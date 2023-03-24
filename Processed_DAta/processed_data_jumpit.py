import boto3
import json
import datetime
import pandas as pd

def processing_jumpit() :
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATMPH7BYJ7OEGGY5J',aws_secret_access_key = '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')

    table = dynamodb.Table('jumpit')
    response = table.scan()

    x=0
    item_list = ['id','회사이름', '연봉','경력','기술스택','회사제목','본문','근무지역','마감일']
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
                    dic['id'] = int('1'+str(item[i]))
                
                elif i == '회사이름' :
                    dic['CompanyName'] = item[i][3:-4]
                    
                elif i == '경력':
                    career = item[i]
                    if career == "무관":
                        dic["Career"] = "경력 무관"
                    else:
                        if career[0] == '신':
                            career = career.replace('신입', "0").replace("년","").replace(" ","")
                            careerList = career.split('-')
                            dic['Career'] = list(map(int,careerList))
                        else :
                            career = career.replace('년','').replace(" ","")
                            careerList = career.split('-')
                            dic['Career'] = list(map(int,careerList))

                elif i == '기술스택' :
                    stacks_list = item[i].split(',')
                    stacks_list.pop()
                    dic['Stacks'] = stacks_list

                elif i == '회사제목' :
                    JobDuty_1 = item[i][4:-5]
                    dic['Job'] = JobDuty_1

                elif i == '본문' :
                    MainData = item[i]
                    dic['MainData'] = MainData
                
                elif i == '근무지역' :
                    Work_Location = item[i]
                    dic['WorkLocation'] = Work_Location

                elif i == '마감일' :
                    Dead_Line = item[i]
                    dic['DeadLine'] = Dead_Line

                else:
                    pass

            except :
                pass

        dic['시간'] = ttime
        dic['Website'] = 'jumpit'
        df = df.append(dic, ignore_index=True)
        # table = dynamodb.Table("ProcessedData")
        # table.put_item(Item=dic)
        # json_data = json.dumps(dic, indent=2, ensure_ascii=False)
        # bucket_name = 'awpsprocesseddata'
        # file_key = f"{dic['id']}.json"
        # s3.put_object(Bucket=bucket_name, Key=file_key, Body=json_data)
        dic = {}
        print(x)
        x+=1
    print(df)
    return df

processing_jumpit()