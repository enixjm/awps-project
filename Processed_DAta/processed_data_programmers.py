import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATMPH7BYJ7OEGGY5J',aws_secret_access_key = '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')

table = dynamodb.Table('programmers')

response = table.scan()
x=0
dic = {}
item_list = ['id','연봉','경력','회사이름']
items = response['Items']
for item in items:
    for x in item_list:
        try:
            if x == '경력':
                career = item[x]
                #if career == "경력 무관":
                    #dic["경력"] = "경력 무관"
                #else:
                career = career.replace("~", "").replace(" 년", "")
                minimum, maximum = career.split()
                dic["최소 경력"] = int(minimum)
                dic["최대 경력"] = int(maximum)

            elif x == '연봉':
                salary = item[x]
                if salary:
                    salary = salary.replace("~", "").replace(" 만원", "")
                    minimum, maximum = salary.split()
                    dic["최소"] = int(minimum)
                    dic["최대"] = int(maximum)
                else:
                    dic["연봉"] = "no data"
            else:
                pass
            print(dic)
        except:
            pass

#for item in items:
    #print(f"id: {item['id']}, career: {item['경력']}, employment type: {item['고용 형태']}, technical stack: {item['기술스택']}, body: {item['본문']}, salary: {item['연봉']}, application deadline: {item['지원 마감']}, job: {item['직무']}, company name: {item['회사이름']}, company title: {item['회사타이틀']}")
    #x+=1
    #print(x)
