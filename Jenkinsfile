pipeline {
    agent { label 'debian' }
    parameters {
        string(name: 'PORT', defaultValue: '5000', description: 'Port pour l\'application')
    }
    stages {
        stage('Build Docker') {
            steps {
                sh 'docker build . -t art_explorer'
            }
        }
        stage('Run Docker') {
            steps {
                sh 'docker rm -f art_explorer || true'
                sh "docker run -d -p ${params.PORT}:5000 --name art_explorer art_explorer"
            }
        }
    }
}
