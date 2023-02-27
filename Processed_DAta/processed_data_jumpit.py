import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATMPH7BYJ7OEGGY5J',aws_secret_access_key = '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')

table = dynamodb.Table('jumpit')

response = table.scan()

x=0
dic = {}
item_list = ['id','회사이름', '연봉','경력','기술스택','회사제목','']
items = response['Items']

#scan()이 한번에 가져올수 있는 용량 제한이 있어 용량 걸렸을때 리스트 확장하는 코드
while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    items.extend(response['Items'])

for item in items:
    salary = None
    for i in item_list:
        try:
            if i == 'id' :
                dic['id'] = int(item[i])
            
            elif i == '회사이름' :            
                dic['CompanyName'] = item[i][3:-4]

            # jumpit에는 연봉데이터가 없음
            # elif i == '연봉':
            #     salary = item[i]
            #     if salary:
            #         salary = salary.replace("~", "").replace(" 만원", "")
            #         payList = salary.split()
            #         dic["연봉"] = list(map(int, payList))
                   
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

                    # career = career.replace("~", "").replace("년", "")
                    # careerLsit = career.split()
                    # dic["경력"] = list(map(int, careerLsit))

            elif i == '기술스택' :
                stacks_list = item[i].split(',')
                stacks_list.pop()
                dic['Stacks'] = stacks_list

            elif i == '회사제목' :
                JobDuty_1 = item[i][4:-5]
                dic['Job'] = JobDuty_1

            

            else:
                pass

        except :
            pass

        
    print(dic)
    table = dynamodb.Table("Processed_jumpit")
    table.put_item(Item=dic)
    dic = {}
    print(x)
    x+=1

