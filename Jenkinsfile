pipeline {
    agent {
        label 'vagrant' // ou tout autre label lié à ton agent Jenkins (machine avec Docker installé)
    }

    parameters {
        string(name: 'PORT', defaultValue: '5000', description: "Port pour l'application")
    }

    environment {
        DOCKER_IMAGE = 'ssh4rk/art-explorer'
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
                script {
                    sh 'sudo docker build . -t $DOCKER_IMAGE:latest'
                }
            }
            post {
                failure {
                    script {
                        sh """
                        curl -X POST -H "Content-Type: application/json" \
                        -d '{"content": "❌ Échec de la phase de build Docker !"}' \
                        "$DISCORD_WEBHOOK"
                        """
                    }
                }
            }
        }

        stage('Tests unitaires') {
            steps {
                script {
                    sh 'sudo docker run --entrypoint=ash $DOCKER_IMAGE:latest -c "python -m pytest tests"'
                }
            }
        }

        stage('Tests avec coverage') {
            steps {
                script {
                    sh 'sudo docker run --entrypoint=ash $DOCKER_IMAGE:latest -c "coverage run -m pytest && coverage report"'
                }
            }
        }

        stage('Déploiement') {
    steps {
        sshagent(['ssh-key-vm']) {
            sh """
            ssh user@vm.example.com '
                docker rm -f art-explorer || true &&
                docker pull $DOCKER_IMAGE:latest &&
                docker run -d -p ${params.PORT}:5000 --name art-explorer $DOCKER_IMAGE:latest
            '
            """
        }
    }
}


    post {
        success {
            script {
                sh """
                curl -X POST -H "Content-Type: application/json" \
                -d '{"content": "✅ Déploiement réussi de Art Explorer sur le port ${params.PORT} !"}' \
                "$DISCORD_WEBHOOK"
                """
            }
        }
        failure {
            script {
                sh """
                curl -X POST -H "Content-Type: application/json" \
                -d '{"content": "🔥 Le pipeline a échoué à un moment donné."}' \
                "$DISCORD_WEBHOOK"
                """
            }
        }
    }
}
s