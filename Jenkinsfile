pipeline {
    agent { label 'vagrant' }

    parameters {
        string(name: 'PORT', defaultValue: '5000', description: "Port pour l'application")
    }

    stages {
        stage('Build') {
            steps {
                sh "sudo docker build . -t art_explorer"
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'sudo docker run --entrypoint=ash art_explorer -c "python -m pytest"'
            }
        }

        stage('Unit Tests with Coverage') {
            steps {
                sh 'sudo docker run --entrypoint=ash art_explorer -c "coverage run -m pytest && coverage report"'
            }
        }

        stage('Deploy on remote VM') {
            steps {
                sshagent(['ssh-key-vm']) {
                    sh """
                    ssh user@vm.example.com '
                      docker rm -f art_explorer || true &&
                      docker pull art_explorer &&
                      docker run -d -p ${params.PORT}:5000 --name art_explorer art_explorer
                    '
                    """
                }
            }
        }
    }
}
