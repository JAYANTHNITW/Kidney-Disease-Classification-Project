# Kidney-Disease-Classification-Project
By Analysing the CT-Scan images we classify whether a kindey has  tumor or not. 

## Watch the video: My Reflection on the Project:
[![Watch the video: My Reflection on Kidney Disease Classification using Dvc and Mlflow](https://img.youtube.com/vi/mmbI1ghn9zQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=mmbI1ghn9zQ)


## Workflows

1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/JAYANTHNITW/Kidney-Disease-Classification-Project.git
```
### STEP 01- Create a conda envinorment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```

### STEP 02- Install the requirements

```bash
pip install -r requirements.txt
```

## MLflow

- [Documenatation](https://www.mlflow.org/docs/2.3.1/index.html)

- [MLflowIntroduction](https://www.youtube.com/watch?v=qdcHHrsXA48)

##### cmd
-mlflow ui

### dagshub
[Dagshub](https://dagshub.com/)

Run this to export as env variables:
 ```bash
export ["MLFLOW_TRACKING_URI"]="https://dagshub.com/JAYANTHNITW/Kidney-Disease-Classification-Project.mlflow"
export ["MLFLOW_TRACKING_USERNAME"]="JAYANTHNITW"
export ["MLFLOW_TRACKING_PASSWORD"]="9e70361d6094119609e2599caf804a1365ab101d"

 ```

### DVC cmd 

1. dvc init
2. dvc repro
3. dvc dag

## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	 
## 3. Create ECR repo to store/save docker image
    - Save the URI: 426633576169.dkr.ecr.ap-southeast-2.amazonaws.com/kidney

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
