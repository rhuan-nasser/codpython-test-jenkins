pipeline{

    agent {

        docker {

            image 'python:latest'
            args '-u root:root'

        }

    }

    stages {

        stage('Verifica se há python instalado!') {
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

        stage('Validação dos códigos do projeto') {
            steps {
                sh 'echo "Diretório atual é o $(pwd)"'
                sh 'echo -e "O conteúdo deste diretório é o \n\n $(ls -l)"'
                sh 'find . -name *.py | xargs pylint -f parseable | tee pylint.log'
            }
        }

        stage('Executando código python') {
            steps {
                sh 'python python.py &'
                sh 'curl localhost:5000'
            }
        }

    }
        
        }