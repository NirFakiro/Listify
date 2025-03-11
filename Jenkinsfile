pipeline {
    agent any

    triggers {
        pollSCM('H/30 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/NirFakiro/My-App-backend.git'
            }
        }

        stage('Setup Virtualenv') {
            steps {
                script {
                    sh '''
                    python -m venv .venv
                    if [ -f ".venv/Scripts/activate" ]; then
                        . .venv/Scripts/activate
                    else
                        source .venv/bin/activate
                    fi
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run backend_testing') {
            steps {
                echo 'Running backend app...'
                sh '. .venv/Scripts/activate && python testing/backend_testing.py'
            }
        }

        stage('Run frontend_testing') {
            steps {
                echo 'Running frontend app...'
                sh '. .venv/Scripts/activate && python testing/frontend_testing.py'
            }
        }

        stage('Clean environment') {
            steps {
                echo 'Cleaning environment...'
                sh '. .venv/Scripts/activate && python clean_environment.py'
            }
        }
    }
}
