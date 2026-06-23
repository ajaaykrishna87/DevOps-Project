pipeline {
agent any

```
environment {
    AWS_REGION = 'eu-north-1'
    ECR_REPO = '805046891242.dkr.ecr.eu-north-1.amazonaws.com/flask-devops-app'
    EC2_HOST = '13.60.29.212'
}

options {
    skipDefaultCheckout(true)
}

stages {

    stage('Checkout') {
        steps {
            git branch: 'main',
            url: 'https://github.com/ajaaykrishna87/DevOps-Project.git'
        }
    }

    stage('Build Docker Image') {
        steps {
            sh 'docker build -t flask-devops-app:${BUILD_NUMBER} .'
        }
    }

    stage('Verify Docker Image') {
        steps {
            sh 'docker images | grep flask-devops-app'
        }
    }

    stage('ECR Login') {
        steps {
            withCredentials([
                string(credentialsId: 'aws-access-key-id', variable: 'AWS_ACCESS_KEY_ID'),
                string(credentialsId: 'aws-secret-access-key', variable: 'AWS_SECRET_ACCESS_KEY')
            ]) {
                sh '''
                aws ecr get-login-password --region $AWS_REGION | \
                docker login --username AWS --password-stdin $ECR_REPO
                '''
            }
        }
    }

    stage('Tag Image') {
        steps {
            sh '''
            docker tag flask-devops-app:${BUILD_NUMBER} \
            $ECR_REPO:${BUILD_NUMBER}
            '''
        }
    }

    stage('Push Image') {
        steps {
            sh '''
            docker push $ECR_REPO:${BUILD_NUMBER}
            '''
        }
    }

    stage('Deploy to EC2') {
        steps {
            sshagent(credentials: ['ec2-ssh-key']) {
                sh '''
                ssh -o StrictHostKeyChecking=no ubuntu@$EC2_HOST "

                aws ecr get-login-password --region eu-north-1 | \
                sudo docker login --username AWS --password-stdin \
                805046891242.dkr.ecr.eu-north-1.amazonaws.com

                sudo docker pull \
                805046891242.dkr.ecr.eu-north-1.amazonaws.com/flask-devops-app:${BUILD_NUMBER}

                sudo docker stop flask-app || true
                sudo docker rm flask-app || true

                sudo docker run -d \
                --name flask-app \
                -p 5000:5000 \
                805046891242.dkr.ecr.eu-north-1.amazonaws.com/flask-devops-app:${BUILD_NUMBER}
                "
                '''
            }
        }
    }
}
```

}
