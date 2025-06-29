pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'ssh4rk'
        IMAGE_NAME = 'art-explorer'
        DISCORD_WEBHOOK = credentials('discord-webhook')
    }

    stages {
        stage('Clonage') {
            steps {
                git 'https://github.com/sSh4rK/art-explorer.git'
            }
        }

        stage('Build de l’image Docker') {
            steps {
                sh 'docker build -t $DOCKER_HUB_USER/$IMAGE_NAME:latest .'
            }
        }

        stage('Push sur Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo "$PASS" | docker login -u "$USER" --password-stdin'
                    sh 'docker push $DOCKER_HUB_USER/$IMAGE_NAME:latest'
                }
            }
        }

        stage('Déploiement local') {
            steps {
                sh 'docker rm -f art-explorer || true'
                sh 'docker run -d --name art-explorer -p 5000:5000 $DOCKER_HUB_USER/$IMAGE_NAME:latest'
            }
        }
    }

    post {
        failure {
            sh '''
            curl -X POST -H "Content-Type: application/json" \
            -d '{"content":"❌ Le pipeline Jenkins a échoué !"}' \
            $DISCORD_WEBHOOK
            '''
        }
    }
}
