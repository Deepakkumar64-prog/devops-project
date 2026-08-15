pipeline {
    agent any

    environment {
        ACCOUNT_ID = '666398468379'
        REGION = 'us-east-1'
        REPO = 'devops-project'
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-project .'
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region $REGION | \
                docker login --username AWS --password-stdin \
                $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com
                '''
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh '''
                docker tag devops-project:latest \
                $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/devops-project:latest
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker push \
                $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/devops-project:latest
                '''
            }
        }
    }
}