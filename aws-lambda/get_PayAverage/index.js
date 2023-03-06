const AWS = require('aws-sdk');

exports.handler = async (event, context, callback) => {
  const dynamodb = new AWS.DynamoDB.DocumentClient();
  const params = {
    TableName: 'ProcessedData',
    ProjectionExpression: 'CompanyName, Pay',
    Limit: 200 // 한번에 가져올 아이템 수
  };

  try {
    let data = [];
    let lastEvaluatedKey = null;

    do {
      // 마지막 평가된 키를 지정하여 다음 페이지 아이템을 가져옴
      if (lastEvaluatedKey) {
        params.ExclusiveStartKey = lastEvaluatedKey;
      }

      const result = await dynamodb.scan(params).promise();

      // 가져온 아이템을 배열에 추가
      data = data.concat(result.Items);

      // 마지막 평가된 키를 업데이트
      lastEvaluatedKey = result.LastEvaluatedKey;
    } while (lastEvaluatedKey);
  
  var TotalMinPay = 0 , TotalMaxPay = 0, num = 0;
  
  for (let i = 0; i < data.length; i++) {
    try {
      TotalMinPay = TotalMinPay + data[i].Pay[0];
      TotalMaxPay = TotalMaxPay + data[i].Pay[1];
      num = num + 1;
    }
    catch (error) {
      continue;
    };
  };
  const AverageMinPay = TotalMinPay / num;
  const AverageMaxPay = TotalMaxPay / num;
  const PayAverage = [AverageMinPay, AverageMaxPay];
  // console.log(AverageMinPay,AverageMaxPay)
  // console.log(data)
    const response = {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify(PayAverage)
    };
    callback(null, response);
  } catch (err) {
    console.log(err);
    const response = {
      statusCode: 500,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify(err)
    };
    callback(null, response);
  }
};
