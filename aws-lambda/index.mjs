export const handler = async(event) => {
    let response;
    const operation = event.httpMethod;
    switch (operation) {
        case 'GET':
            let data = {
                'id': 1,
                'name': '최소현'
            }
            response = {
                statusCode: 200,
                headers: { 'Access-Control-Allow-Origin': '*' },
                body: JSON.stringify(data)
            };
            break;
        case 'POST':
            response = {
                statusCode: 200
            };
            break;
    }
    // response = {
    //     statusCode: 200,
    //     body: JSON.stringify("->"+operation)
    // };
    return response;
    

};
