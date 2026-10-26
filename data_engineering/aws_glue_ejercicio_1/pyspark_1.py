"""AWS Glue ETL job (PySpark): reads raw reviews from the Data Catalog, filters and
enriches them, and writes the result to S3 as Parquet."""

import sys
from pyspark.context import SparkContext
from pyspark.sql.functions import col, length, to_timestamp
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

# OUTPUT_PATH is passed as a job argument (--OUTPUT_PATH s3://my-bucket/processed/)
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Standard Glue job skeleton: init enables bookmarks/metrics, commit at the end
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read raw data
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="product_reviews_db",
    table_name="raw_reviews",
    transformation_ctx="datasource"
)

# Convert to DataFrame for transformations
df = datasource.toDF()

# Clean and transform data
df_clean = (
    df
    .filter(col("review_text").isNotNull())
    .filter(col("review_rating") >= 3)
    .withColumn("review_date", to_timestamp("review_date"))
    .withColumn("review_length", length("review_text"))
)

# Convert back to DynamicFrame
final_df = DynamicFrame.fromDF(df_clean, glueContext, "final_df")

# Write to S3 in Parquet format
glueContext.write_dynamic_frame.from_options(
    frame=final_df,
    connection_type="s3",
    connection_options={"path": args['OUTPUT_PATH']},
    format="parquet"
)

job.commit()
