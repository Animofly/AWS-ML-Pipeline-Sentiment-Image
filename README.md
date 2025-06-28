# AWS-ML-Pipeline-Sentiment-Image
# AWS Machine Learning Pipeline: Sentiment & Image Classification

## Project Overview
This project demonstrates an end-to-end Machine Learning pipeline on AWS, handling both text sentiment analysis and image classification using Amazon SageMaker and AWS AI Services.

### Key Features:
- Data storage using Amazon S3
- Model training and deployment using Amazon SageMaker
- Sentiment analysis using Amazon Comprehend and custom-trained model
- Image classification using Amazon Rekognition and custom CNN model
- Real-time prediction using SageMaker Endpoints

---

## Project Structure
- **text_model/**: Jupyter notebooks and code for sentiment analysis model training.
- **image_model/**: Jupyter notebooks and code for image classification model training.
- **aws_ai_services/**: Code to integrate Amazon Comprehend and Rekognition.
- **deployment/**: Code for model deployment and API testing.
- **datasets.txt**: Links to the datasets used.

---

## Tools & Services
- Amazon S3
- Amazon SageMaker
- Amazon Comprehend
- Amazon Rekognition
- Python (boto3, pandas, sklearn, TensorFlow)

---

## Deployment Architecture
(Add your architecture diagram here or describe as below)
- Data stored in Amazon S3
- Model training and deployment on SageMaker
- Real-time predictions through SageMaker Endpoints
- AWS Comprehend and Rekognition for comparison

---

## Dataset Sources
- [Amazon Product Reviews Dataset](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- [CIFAR-10 Image Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)

---

## Project Status
✔️ Model training scripts  
✔️ SageMaker deployment ready  
✔️ AWS AI services integration  
✔️ API testing (in progress)
