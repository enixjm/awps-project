const AWS = require('aws-sdk');
const s3 = new AWS.S3();

exports.handler = async (event, context, callback) => {
  const params = {
    Bucket: 'awpsapidata',
    Key: 'TotalStacks.json'
  };
  
  try {
    const data = await s3.getObject(params).promise();
    console.log(data.Body.toString('utf-8')); // S3 객체 내용 출력
    const dataString = data.Body.toString('utf-8')
    const dataObject = JSON.parse(dataString)
    
    const response = {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify(dataObject)
    };
    callback(null, response)
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
    callback(null, response)
  };
};
