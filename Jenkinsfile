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
                sh 'docker images'
            }
        }

        stage('Verify Environment') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }
    }
}
