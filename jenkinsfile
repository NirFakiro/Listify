pipeline {
    agent any


    triggers {
        pollSCM('H/30 * * * *')
    }


    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }

    stages {
        stage('Checkout') {
            steps {

                git branch: 'main', url: 'https://github.com/NirFakiro/My-App-backend.git'
            }
        }

        stage('Run backend_testing') {
            steps {
                echo 'Running backend app...'
                sh 'python3 testing/backend_testing.py'
            }
        }

        stage('Run frontend_testing') {
            steps {
                echo 'Running frontend app...'
                sh 'python3 testing/frontend_testing.py'
            }
        }

        stage('Clean environment') {
            steps {
                echo 'Cleaning environment...'
                sh 'python3 clean_environment.py'
            }
        }
    }
}
