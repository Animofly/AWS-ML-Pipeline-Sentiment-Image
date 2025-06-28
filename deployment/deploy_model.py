import boto3

sagemaker = boto3.client('sagemaker')
response = sagemaker.create_endpoint_config(
    EndpointConfigName='TextModelEndpointConfig',
    ProductionVariants=[
        {
            'VariantName': 'AllTraffic',
            'ModelName': 'text-model',
            'InitialInstanceCount': 1,
            'InstanceType': 'ml.t2.medium',
        },
    ],
)

response = sagemaker.create_endpoint(
    EndpointName='TextModelEndpoint',
    EndpointConfigName='TextModelEndpointConfig'
)
