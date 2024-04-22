import streamlit

import random
import pandas as pd
import boto3
import os
from io import StringIO
import streamlit as st

def generatedata():
    months = ['1-Jan', '2=Feb', '3-Mar', '4-Apr']
    stores = ['Fudgemart', 'Mikeazon']
    departments = ['Doodads', 'Niknaks', 'Widgets']
    measures = { 
                'Sold' : { 'min' :50, 'max' : 290}, 
                'Returned': { 'min': 0, 'max': 50},
                'Ordered' : { 'min': 0, 'max': 100}
                }

    rows = []
    for m in months:
        for d in departments:
            for s in stores:
                sold = random.randint(measures['Sold']['min'], measures['Sold']['max'])
                returned = random.randint(measures['Returned']['min'], measures['Returned']['max'])
                ordered = random.randint(measures['Ordered']['min'], measures['Ordered']['max'])
                row = {'Month': m, 'Dept': d, 'Store': s, 'Sold': sold, 'Returned': returned, 'Ordered': ordered}
                rows.append(row)
    return rows

def soft_create_bucket(s3, bucket_name):
    # Output the bucket names
    response = s3.list_buckets()
    for bucket in  response['Buckets']:
        if bucket['Name'] == bucket_name:
            return
    s3.create_bucket(Bucket=bucket_name)

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
    df.to_csv(csv_buffer, index=False, header=True)
    s3r.Object(bucket_name, file_name).put(Body=csv_buffer.getvalue())
    

## Main
bucket_name = os.environ.get("MINIO_BUCKET", "data")
file_name = os.environ.get("DATA_SOURCE","companydata.csv")
s3 = boto3.client('s3', 
    endpoint_url=os.environ['MINIO_URL'],
    aws_access_key_id=os.environ['MINIO_USER'],
    aws_secret_access_key=os.environ['MINIO_PASSWORD'],
    aws_session_token=None,
    config=boto3.session.Config(signature_version='s3v4'),
    verify=False
)

soft_create_bucket(s3, bucket_name)

st.title("Data Pipeline Data Generator")
if st.button("Regenerate Data"):
    df = pd.DataFrame(generatedata())
    write_to_bucket(df, bucket_name, file_name)
    st.dataframe(df, use_container_width=True)
