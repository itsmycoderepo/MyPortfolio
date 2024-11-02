import boto3
import requests
import boto3
import json

# Initialize the SageMaker runtime client
runtime_client = boto3.client('sagemaker-runtime', region_name='us-east-1')

# Define your endpoint name
endpoint_name = 'ml-model-endpoint'

# Your input payload for the model
payload = {
    "instances": [
        {"features": [311,104,3,4.5,4.5,8.43,0]}  # Replace with your actual data structure
    ]
}

# Convert the payload to JSON format
data = json.dumps(payload)

# Invoke the SageMaker endpoint
response = runtime_client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType='application/json',
    Body=data
)

# Parse the response
result = json.loads(response['Body'].read().decode())

# Print the result
print("\n",result)