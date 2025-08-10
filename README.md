This Machine Learning Web Application uses a several features of Banknotes like variance, skewness, curtosis and entropy to predict the Authenticy of Banknotes weither it is Genuine or Forged with an accuracy of 99.02% using Random Forest Classifier.This Dataset is taken from UCI Repository and also available in Kaggle,Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images,In this ml model we are considering 0 for geniune bank note and 1 for forged bank note.

Purpose of the Project:
Money is central to everyday transactions, whether through paper bills, coins, or credit cards. While most modern money exists as electronic records in banks, physical currency remains crucial for daily use. This project focuses on understanding and addressing issues related to currency in circulation.

Why Banknote Genuineness Is Important?

Genuine banknotes are essential to maintain trust in the currency, protect the economy from counterfeiting, prevent financial loss for individuals and businesses, and combat crime linked to fake money. Ensuring authenticity keeps transactions smooth, stable, and secure.

We have used Random Forest Classifier with Sklearn library. 

Technology Stack

    SkLearn
    Streamlit
    Flask
    Swagger UI
    Docker
    Kubernetes

Building docker image:
1. To build an image:
docker build -t money_api .
2. To list the images:
docker images
3. To create a container:
docker run -p 8000:8000 money_api
4. To build an image and push it to docker hub:
docker build -t <username>/money_api:0.0.1 .
docker login
docker push <username>/money_api:0.0.1

Deploying in Kubernetes:
1. To get the nodes:
kubectl get nodes
2. To create resources in cluster as defined in deploy.yml
kubectl apply -f deploy.yml
3. To get the pods:
kubectl get pods
4. To get the available services:
kubectl get svc
5. To access the pod inside the cluster from local machine:
kubectl port-forward svc/money-api-service 1111:80 --address=0.0.0.0

To view the application:
http://localhost:1111/apidocs
