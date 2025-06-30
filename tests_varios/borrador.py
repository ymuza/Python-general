import boto3
import logging
import csv
import io




def transform_is_active_column(csv_content):
    """
    Transforms 'is_active' column values: 0 -> 'No', 1 -> 'Yes'
    """
    input_io = io.StringIO(csv_content)
    output_io = io.StringIO()

    reader = csv.DictReader(input_io)
    fieldnames = reader.fieldnames

    if "is_active" not in fieldnames:
        logger.warning("No 'is_active' column found.")
        return csv_content  # return unchanged

    writer = csv.DictWriter(output_io, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        if row["is_active"] == "0":
            row["is_active"] = "No"
        elif row["is_active"] == "1":
            row["is_active"] = "Yes"
        writer.writerow(row)

    return output_io.getvalue()





logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        record = event['Records'][0]
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']

        logger.info(f"Received file: s3://{bucket_name}/{object_key}")

        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        file_content = response['Body'].read().decode('utf-8')

        # Transform the CSV content
        transformed_csv = transform_is_active_column(file_content)

        logger.info("Transformed CSV content:")
        logger.info("\n" + transformed_csv)

        return {
            "statusCode": 200,
            "body": f"Processed file: {object_key}"
        }

    except Exception as e:
        logger.error("Error processing file", exc_info=True)
        return {
            "statusCode": 500,
            "body": str(e)
        }
