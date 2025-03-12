pipeline {
    agent {
        docker {
            image 'python:3.12'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing dependencies from requirements.txt..."
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Server') {
            steps {
                dir('user_api') {
                    script {
                        echo "Running server.py..."
                        sh 'python server.py'
                    }
                }
            }
        }
    }
}
