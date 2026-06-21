pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code checkout successful'
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
