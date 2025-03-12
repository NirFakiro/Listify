pipeline {
    agent {
        docker {
            image 'python:3.12'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Server') {
            steps {
                dir('user_api') {
                    sh 'python server.py'
                }
            }
        }
    }
}
