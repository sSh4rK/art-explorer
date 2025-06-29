pipeline {
    agent { label 'Debian' }

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
                    sh '''
                        docker rm -f art_explorer || true
                        docker run --rm -d -p 9000:9000 -e PORT=9000 --name art_explorer art_explorer
                    '''
                }
            }
        }
    }
}
