const AWS = require('aws-sdk');

exports.handler = async (event, context, callback) => {
  const dynamodb = new AWS.DynamoDB.DocumentClient();
  const params = {
    TableName: 'Processed_programmers'
  };

  try {
    const data = await dynamodb.scan(params).promise();
    const response = {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify(data.Items)
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