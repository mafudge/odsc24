import pandas as pd
import os
import boto3
from io import StringIO
from time import sleep


def transformation(source_df):
    data_selection = data[['Dept', 'Sold', 'Returned', 'Ordered']]
    data_summary = data_selection.groupby(["Dept"]).sum()
    return data_summary 
    
def get_etag(s3, bucket_name, file_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    for object in response['Contents']:
        if object['Key'] == file_name:
            return object.get("ETag", "")
    return ""

def write_to_bucket(df, bucket_name, file_name):
    s3r = boto3.resource('s3', 
        endpoint_url=os.environ['MINIO_URL'],
        aws_access_key_id=os.environ['MINIO_USER'],
        aws_secret_access_key=os.environ['MINIO_PASSWORD'],
        aws_session_token=None,
        config=boto3.session.Config(signature_version='s3v4'),
        verify=False
    )
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=True, header=True)
    s3r.Object(bucket_name, file_name).put(Body=csv_buffer.getvalue())
  

bucket_name = os.environ.get("MINIO_BUCKET", "data")
source_file = os.environ.get("DATA_SOURCE","companydata.csv")
target_file = os.environ.get("DATA_TARGET","dashboarddata.csv")
s3 = boto3.client('s3', 
    endpoint_url=os.environ['MINIO_URL'],
    aws_access_key_id=os.environ['MINIO_USER'],
    aws_secret_access_key=os.environ['MINIO_PASSWORD'],
    aws_session_token=None,
    config=boto3.session.Config(signature_version='s3v4'),
    verify=False
)

current_etag = "unknown"
while True:
    sleep(2)
    new_etag = get_etag(s3, bucket_name, source_file)
    if  current_etag != new_etag:
        print("Processing file change...")
        #New File: Read it
        obj = s3.get_object(Bucket=bucket_name, Key=source_file)
        data = pd.read_csv(obj['Body'])
        
        # Transform it
        data_summary = transformation(data)
        
        # Write out transformation
        write_to_bucket(data_summary, bucket_name, target_file)
        print(data_summary)
        
        #update Etag
        current_etag = new_etag
    else:
        pass # maybe some logging here?

