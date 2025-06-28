import boto3

client = boto3.client('rekognition')
image_bucket = 'your-s3-bucket'
image_name = 'sample_image.jpg'

response = client.detect_labels(
    Image={'S3Object': {'Bucket': image_bucket, 'Name': image_name}},
    MaxLabels=5
)

for label in response['Labels']:
    print(f"{label['Name']}: {label['Confidence']:.2f}%")
