pipeline {
    agent any
    stages {
        /*stage('version') {
            steps {
                sh 'python --version'
            }
        }
        stage('hello') {
            steps {
                sh 'python Hello.py'
            }
        }*/
        stage('Echo Hello') {
            steps {
                echo 'Hello'
            }
        }

        stage('Running Files') {
            steps {
                python3 Hello.py
            }
        }
    }
}