pipeline {
    agent {
        label 'Debian'
    }

    environment {
        DOCKER_IMAGE = 'art_explorer'
        CONTAINER_NAME = 'art_explorer'
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'docker run --rm $DOCKER_IMAGE python -m pytest tests'
            }
        }

        stage('Run Unit Tests with Coverage') {
            steps {
                sh '''
                    docker run --rm $DOCKER_IMAGE sh -c "coverage run -m pytest && coverage report"
                '''
            }
        }

        stage('Run Application') {
            steps {
                script {
                    // Supprimer le conteneur si existant
                    sh 'docker rm -f $CONTAINER_NAME || true'

                    // Tuer le processus si le port est occupé
                    sh '''
                        echo ">> Vérification du port $APP_PORT"
                        PID=$(lsof -ti tcp:$APP_PORT)
                        if [ ! -z "$PID" ]; then
                          echo ">> Port $APP_PORT utilisé par PID: $PID. Suppression..."
                          kill -9 $PID || true
                          sleep 2
                        else
                          echo ">> Port $APP_PORT libre."
                        fi
                    '''

                    // Boucle d’attente jusqu’à libération du port
                    sh '''
                        echo ">> Attente que le port $APP_PORT soit libre..."
                        while lsof -i :$APP_PORT >/dev/null; do
                          echo ">> En attente..."
                          sleep 1
                        done
                    '''

                    // Lancer le conteneur
                    sh 'docker run -d -p $APP_PORT:$APP_PORT --name $CONTAINER_NAME $DOCKER_IMAGE'

                    // (Optionnel) Vérifie que l’app répond
                    sh '''
                        echo ">> Vérification que l’application est en ligne..."
                        sleep 3
                        curl -f http://localhost:$APP_PORT || (echo ">> Erreur : l’application ne répond pas." && exit 1)
                    '''
                }
            }
        }
    }
}
