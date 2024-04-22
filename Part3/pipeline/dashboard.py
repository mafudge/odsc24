import streamlit

import pandas as pd
import boto3
import os
from time import sleep
import streamlit as st

def get_etag(s3, bucket_name, file_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    for object in response['Contents']:
        if object['Key'] == file_name:
            return object.get("ETag", "")
    return ""

bucket_name = os.environ.get("MINIO_BUCKET", "data")
target_file = os.environ.get("DATA_TARGET","dashboarddata.csv")
s3 = boto3.client('s3', 
    endpoint_url=os.environ['MINIO_URL'],
    aws_access_key_id=os.environ['MINIO_USER'],
    aws_secret_access_key=os.environ['MINIO_PASSWORD'],
    aws_session_token=None,
    config=boto3.session.Config(signature_version='s3v4'),
    verify=False
)

obj = s3.get_object(Bucket=bucket_name, Key=target_file)
data = pd.read_csv(obj['Body'])
st.title("Data Pipeline Dashboard")
st.dataframe(data)
st.bar_chart(data, x="Dept", y="Sold")

current_etag = "unknown"
while True:
    sleep(2)
    new_etag = get_etag(s3, bucket_name, target_file)
    if current_etag != new_etag:
        current_etag = new_etag
        st.rerun()
    
