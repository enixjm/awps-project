import os

import boto3
import pandas as pd
import json

s3 = boto3.resource('s3')
bucket_name = 'processedjumpit'

bucket = s3.Bucket(bucket_name)

df = pd.DataFrame()

for obj in bucket.objects.all():
    json_string = obj.get()['Body'].read().decode('utf-8')
    json_dict = json.loads(json_string)
    df = df.append(json_dict, ignore_index=True)
    print(df)

# obj = s3.Object(bucket_name, '9991.json')
# response = obj.get()

# print(response['Body'].read().decode('utf-8'))



# s3_client = boto3.client("s3")

# response = s3_client.get_object(Bucket='processedjumpit', Key="10026.json")

# status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

# if status == 200:
#     print(f"Successful S3 get_object response. Status - {status}")
#     books_df = pd.read_csv(response.get("Body"))
#     print(books_df)
# else:
#     print(f"Unsuccessful S3 get_object response. Status - {status}")