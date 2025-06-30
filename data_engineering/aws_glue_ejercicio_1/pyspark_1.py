# Glue ETL Script (PySpark)
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, length, to_timestamp

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

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
    connection_options={"path": "s3://your-bucket-name/processed/"},
    format="parquet"
)
