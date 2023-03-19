from processed_data_jumpit import processing_jumpit
from processed_data_programmers import processing_programemrs
import pandas as pd
import boto3


jumpit_df = processing_jumpit()
programmers_df = processing_programemrs()
df = pd.concat([programmers_df,jumpit_df])
df = df.set_index('id')

print(df)

csv = df.to_csv('C:/Users/홍성학/Desktop/AWPS/awps-project/Processed_DAta/all_data.csv',index=False)

s3 = boto3.client('s3')
file_name = 'all_data.csv'

bucket_name = 'awpsprocesseddata'

s3.upload_file(file_name,bucket_name,file_name)