import boto3
import json
import datetime
import pandas as pd

def processing_programemrs() :
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATMPH7BYJ7OEGGY5J',aws_secret_access_key = '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')

    table = dynamodb.Table('programmers')

    response = table.scan()
    x=0
    item_list = ['id','회사이름','연봉','경력','기술스택','직무','본문','근무지역','마감일']
    items = response['Items']

    df = pd.DataFrame(
        columns=['id','CompanyName',"Pay","Career" ,'Stacks','Job','MainData','WorkLocation','DeadLine','시간','Website']
    )

    #scan()이 한번에 가져올수 있는 용량 제한이 있어 용량 걸렸을때 리스트 확장하는 코드
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response['Items'])

    for item in items:
        dic = {}
        now = datetime.datetime.now()
        ttime = now.strftime("%y-%m-%d %H:%M:%S")
        salary = None
        for i in item_list:
            try:
                if i == 'id' :
                    dic['id'] = int('2'+str(item[i]))

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

                elif i == '본문' :
                    MainData = item[i]
                    dic['MainData'] = MainData

                elif i == '근무지역' :
                    Work_Location = item[i]
                    dic['WorkLocation'] = Work_Location

                elif i == '마감일' :
                    Dead_Line = item[i]
                    dic['DeadLind'] = Dead_Line

                else:
                    pass

            except :
                pass

        dic['시간'] = ttime
        dic['Website'] = 'programmers'
        df = df.append(dic, ignore_index=True)

        dic = {}
        print(x)
        x+=1
    print(df)
    return df