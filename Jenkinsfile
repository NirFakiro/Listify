pipeline {
    agent any

    stages {
        stage('Check Python Version') {
            steps {
                script {
                    echo "Checking Python version..."
                    sh 'python --version'
                    echo "Python is working fine."
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing dependencies from requirements.txt..."
                    sh 'pip install -r requirements.txt'
                    echo "Dependencies installed successfully."
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
