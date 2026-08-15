pipeline {
    agent any

    environment {
        ACCOUNT_ID = '666398468379'
        REGION = 'us-east-1'
        REPO = 'devops-project'
        AWS_PAGER = ''
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ${REPO} .
                '''
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region ${REGION} | \
                docker login --username AWS --password-stdin \
                ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com
                '''
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh '''
                docker tag ${REPO}:latest \
                ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPO}:latest
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker push \
                ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPO}:latest
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-ssh-key']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no root@107.21.85.47 \
                    "cd ~ && ./deploy.sh"
                    '''
                }
            }
        }
    }
}