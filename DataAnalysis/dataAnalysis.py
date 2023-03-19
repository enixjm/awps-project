import pandas as pd
import numpy as np
import json
import boto3
import ast
from collections import Counter

df = pd.read_csv('all_data.csv', index_col=0)
df['id'] = df['id'].astype(int)
df = df.set_index('id')

s3 = boto3.client('s3')

def get_TotalStacks(df) :
    dic = {}
    for i in df['Stacks'] :
        list = i.split(',')
        for j in list :
            j = j.replace("'",'').replace(' ','').replace('[','').replace(']','')
            if j in dic :
                dic[j] += 1
            else :
                dic[j] = 1
    del dic['']
    SortedDic_list = sorted(dic.items(),reverse=True,key=lambda item: item[1])
    dic2 = {}
    for key,value in SortedDic_list :
        dic2[key] = value
    json_data = json.dumps(dic2,indent=2,ensure_ascii = False)
    bucket_name = 'awpsapidata'
    file_key = "TotalStacks.json"
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=json_data)
    return dic2


def get_job_tech_ranking(df):
    d = {}
    for index, row in df.iterrows():
        for key in ast.literal_eval(row['Job']):
            if not key in d:
                d[key] = []
            d[key].extend(ast.literal_eval(row['Stacks']))
    ret = {}
    for key, val in d.items():
        ret[key] = Counter(val).most_common()

    json_data = json.dumps(ret,indent=2,ensure_ascii = False)
    bucket_name = 'awpsapidata'
    file_key = "TechRanking_ByJob.json"
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=json_data)
    return ret

get_TotalStacks(df)
get_job_tech_ranking(df)