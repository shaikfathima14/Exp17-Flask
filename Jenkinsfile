pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Build') {
            steps {
                bat 'python --version'
                bat 'pip --version'
                echo 'Build completed successfully.'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Application deployed successfully.'
            }
        }
    }
}