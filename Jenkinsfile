pipeline {
    agent {
        label 'vagrant' // Ou 'Debian' selon ton agent
    }

    environment {
        PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
                    // Supprimer l'ancien conteneur s'il existe
                    sh 'docker rm -f art_explorer || true'

                    // Libérer le port si déjà utilisé (nécessite `psmisc` pour fuser)
                    sh 'fuser -k ${PORT}/tcp || true'

                    // Lancer l’application dans un conteneur détaché
                    sh 'docker run -d -p ${PORT}:5000 --name art_explorer art_explorer'
                }
            }
        }
    }
}
