pipeline{
    agent {
        docker {
            image: 'python:latest'
        }
    }

    stages {
        stage('Validações') {
            steps {
                sh 'python --version'
                sh 'pip --version'
                  }
                       }
           }
        }