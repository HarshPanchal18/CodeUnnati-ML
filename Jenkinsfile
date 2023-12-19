pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                bash 'python --version'
            }
        }
        stage('hello') {
            steps {
                bash 'python Hello.py'
            }
        }
    }
}