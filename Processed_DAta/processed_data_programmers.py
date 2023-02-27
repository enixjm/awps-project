import boto3
import json
import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATMPH7BYJ7OEGGY5J',aws_secret_access_key = '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')

access_key = 'AKIATMPH7BYJ7OEGGY5J'
secret_key = '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'
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
table = dynamodb.Table('programmers')

response = table.scan()
x=0
dic = {}
item_list = ['id','회사이름','연봉','경력','기술스택','직무']
items = response['Items']

#scan()이 한번에 가져올수 있는 용량 제한이 있어 용량 걸렸을때 리스트 확장하는 코드
while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    items.extend(response['Items'])

for item in items:
    now = datetime.datetime.now()
    ttime = now.strftime("%y-%m-%d %H:%M:%S")
    salary = None
    for i in item_list:
        try:
            if i == 'id' :
                dic['id'] = int(item[i])

            elif i == '회사이름' :
                dic['CompanyName'] = item[i]

            elif i == '연봉':
                salary = item[i]
                if salary:
                    salary = salary.replace("~", "").replace(" 만원", "")
                    payList = salary.split()
                    dic["Pay"] = list(map(int, payList))
                   
            elif i == '경력':
                career = item[i]
                if career == "경력 무관":
                    dic["Career"] = "경력 무관"
                else:
                    career = career.replace("~", "").replace("년", "")
                    careerLsit = career.split()
                    dic["Career"] = list(map(int, careerLsit))

            elif i == '기술스택' :
                stacks_list = item[i].split(',')
                stacks_list.pop()
                dic['Stacks'] = stacks_list
                
            elif i == '직무' :
                JobDuty = item[i].split(',')
                dic['Job'] = JobDuty

            else:
                pass

        except :
            pass

    dic['시간'] = ttime
    print(dic)
    json_data = json.dumps(dic,indent=2,ensure_ascii = False)
    bucket_name = 'processedprogrammers'
    file_key = f"{dic['id']}.json"
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=json_data)
    dic = {}
    print(x)
    x+=1

