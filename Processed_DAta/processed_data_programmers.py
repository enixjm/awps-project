import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATMPH7BYJ7OEGGY5J',aws_secret_access_key = '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')

table = dynamodb.Table('programmers')

response = table.scan()
x=0
dic = {}
item_list = ['id','연봉','경력','회사이름']
items = response['Items']
for item in items:
    salary = None
    for i in item_list:
        try:
            if i == 'id' :
                dic['id'] = int(item[i])
            elif i == '연봉':
                salary = item[i]
                if salary:
                    salary = salary.replace("~", "").replace(" 만원", "")
                    minimum, maximum = salary.split()
                    dic["최소 연봉"] = int(minimum)
                    dic["최대 연봉"] = int(maximum)
                    

            elif i == '경력':
                career = item[i]
                #if career == "경력 무관":
                    #dic["경력"] = "경력 무관"
                #else:
                career = career.replace("~", "").replace("년", "")
                mininum , maxinum = career.split()
                dic["최소 경력"] = int(mininum)
                dic["최대 경력"] = int(maxinum)
            
            else:
                pass

        except:
            pass
    print(dic)
    dic = {}
#for item in items:
    #print(f"id: {item['id']}, career: {item['경력']}, employment type: {item['고용 형태']}, technical stack: {item['기술스택']}, body: {item['본문']}, salary: {item['연봉']}, application deadline: {item['지원 마감']}, job: {item['직무']}, company name: {item['회사이름']}, company title: {item['회사타이틀']}")
    #x+=1
    #print(x)
