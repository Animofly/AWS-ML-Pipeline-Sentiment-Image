import boto3

client = boto3.client('comprehend')
text = "I love this product, it works great!"

response = client.detect_sentiment(
    Text=text,
    LanguageCode='en'
)

print("Sentiment:", response['Sentiment'])
