pipeline {
    agent { label 'Debian' } // adapte ce label à celui de ton agent

    parameters {
        string(name: 'PORT', defaultValue: '5000', description: 'Port pour l’application')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: 'refs/heads/main']],
                    userRemoteConfigs: [[url: 'https://github.com/sSh4rK/art-explorer.git']]])
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t art_explorer .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'docker run --rm art_explorer python -m pytest tests'
            }
        }

        stage('Run Unit Tests with Coverage') {
            steps {
                sh 'docker run --rm art_explorer sh -c "coverage run -m pytest && coverage report"'
            }
        }

        stage('Run Application') {
            steps {
                script {
                    sh 'docker rm -f art_explorer || true' // supprime le conteneur si il existe
                    sh "docker run -d -p ${params.PORT}:5000 --name art_explorer art_explorer"
                }
            }
        }
    }
}
