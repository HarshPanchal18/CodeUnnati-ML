pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                bat 'bash python --version'
            }
        }
        stage('hello') {
            steps {
                bat 'bash python Hello.py'
            }
        }
    }
}