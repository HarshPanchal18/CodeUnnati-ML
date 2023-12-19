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
        stage('Echo Hello World') {
            steps {
                echo 'Hello'
                echo ' World'
            }
        }

        stage('Running Files') {
            steps {
                //python3 Hello.py
                sh(script: 'python3 --version || echo Ending')
            }
        }
    }
}