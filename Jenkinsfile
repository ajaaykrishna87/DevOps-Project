pipeline {
    agent any

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
    }
}
