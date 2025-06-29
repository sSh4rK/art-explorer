pipeline {
    agent {
        label 'Debian'  // le label de ton agent Debian dans Jenkins
    }

    parameters {
        string(name: 'PORT', defaultValue: '5000', description: "Port pour l'application")
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sSh4rK/art-explorer.git'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build . -t art_explorer'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'docker run --rm --entrypoint=ash art_explorer -c "python -m pytest"'
            }
        }

        stage('Run Unit Tests with Coverage') {
            steps {
                sh 'docker run --rm --entrypoint=ash art_explorer -c "coverage run -m pytest && coverage report"'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker rm -f art_explorer || true'
                sh "docker run -d -p ${params.PORT}:5000 --name art_explorer art_explorer"
            }
        }
    }
}
