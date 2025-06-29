pipeline {
    agent {
        label 'Debian'
    }

    environment {
        PORT = '5000'
        CONTAINER_NAME = 'art_explorer'
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
                    // Stop any container with same name
                    sh 'docker rm -f $CONTAINER_NAME || true'

                    // Kill any process using the port (host level)
                    sh '''
                        echo ">> Checking if port $PORT is in use"
                        if lsof -i :$PORT; then
                          echo ">> Port $PORT in use, killing process..."
                          fuser -k ${PORT}/tcp || true
                          sleep 2
                        fi
                    '''

                    // Wait until the port is really free
                    sh '''
                        echo ">> Waiting for port $PORT to be free..."
                        while lsof -i :$PORT >/dev/null; do
                          sleep 1
                        done
                    '''

                    // Run the container
                    sh 'docker run -d -p $PORT:5000 --name $CONTAINER_NAME art_explorer'
                }
            }
        }
    }
}
