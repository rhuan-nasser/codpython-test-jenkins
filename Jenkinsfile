pipeline{
    agent {
        docker {
            image 'python:latest'
        }
    }

    stages {
        stage('Validações') {
            steps {
                sh 'python --version'
                sh 'pip --version'
            }
        }
        
        stage('Instalando libs do requirements.txt') {
            steps {
                sh 'pip install -r requirements.txt --no-cache-dir --disable-pip-version-check'
            }
        }
    }
        
        }