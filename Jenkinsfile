pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/YOUR_USERNAME/aws-devops-online-booking-system.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t booking-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 booking-app'
            }
        }
    }
}
