pipeline {
    agent any

    tools {
        python 'python 3.12'
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
