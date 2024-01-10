import boto3

lambda_client = boto3.client('lambda')

lambda_function = lambda_client.create_function(
    FunctionName='NotificarAcessoDynamoDB',
    Runtime='python3.8',
    Role='arn:aws:iam::869923096763:role/verifica-acesso001',
    Handler='lambda_function.lambda_handler',
    Code={
        'S3Bucket': 'arn:aws:s3:::lambda-emite-email',
        #'S3Key': 'your_lambda_code.zip'
    },
    Environment={
        'Variables': {
            'DESTINATION_EMAIL': 'exemplo.lambda@gmail.com'
        }
    }
)

lambda_client.add_permission(
    FunctionName=lambda_function['FunctionName'],
    StatementId='ID',
    Action='lambda:InvokeFunction',
    Principal='apigateway.amazonaws.com'
)
