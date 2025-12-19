pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/pragadasathya/newproject.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t booking-app:latest .
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker rm -f booking-app || true
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker run -d --name booking-app -p 5000:5000 booking-app:latest
                '''
            }
        }
    }
}
