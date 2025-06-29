pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: 'refs/heads/main']],
                          userRemoteConfigs: [[url: 'https://github.com/sSh4rK/art-explorer.git']]])
            }
        }
        stage('Test') {
            steps {
                echo "Le checkout a réussi, on a le code !"
            }
        }
    }
}
