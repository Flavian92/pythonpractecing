execution_role = {
    'RoleArn': role_arn,
    'RoleName': 'lambda_execution_role'
}

# Lambda function configuration
function_configuration = {
    'FunctionName': function_name,
    'Runtime': 'python3.8',
    'Role': role_arn,
    'Handler': 'lambda_function.lambda_handler',  # Python file name and handler function
    'Code': {
        'S3Bucket': s3_bucket,
        'S3Key': s3_key
    },
    'Description': 'Your Lambda function description',
    'Timeout': 10,  # Maximum function execution time in seconds
    'MemorySize': 128  # Maximum amount of memory the function can use in MB
}

# Create an IAM client
iam_client = boto3.client('iam')

# Create Lambda execution role
iam_client.create_role(**execution_role)

# Create a Lambda client
lambda_client = boto3.client('lambda')

# Create Lambda function
lambda_client.create_function(**function_configuration)

print(f'Lambda function "{function_name}" created successfully.')