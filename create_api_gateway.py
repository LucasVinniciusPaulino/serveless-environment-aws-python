
import boto3

apigateway = boto3.client('apigateway')

api = apigateway.create_rest_api(
    name='colorAPI',
    description='API para acesso a cores'
)

resource = apigateway.create_resource(
    restApiId=api['id'],
    parentId=api['rootResourceId'],
    pathPart='cores'
)

method = apigateway.put_method(
    restApiId=api['id'],
    resourceId=resource['id'],
    httpMethod='POST',
    authorizationType='AWS_IAM'
)

apigateway.put_method_response(
    restApiId=api['id'],
    resourceId=resource['id'],
    httpMethod='POST',
    statusCode='200',
    responseModels={'application/json': 'Empty'}
)

apigateway.put_integration(
    restApiId=api['id'],
    resourceId=resource['id'],
    httpMethod='POST',
    type='AWS_PROXY',
    integrationHttpMethod='POST',
    uri='arn:aws:apigateway:{755674844232}:lambda:path/2015-03-31/functions/{lambda_arn}/invocations'
   #uri='arn:aws:apigateway:{region}:lambda:path/2015-03-31/functions/{lambda_arn}/invocations'
)
