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
            }

            steps {
                echo 'World'
            }
        }

        stage('Running Files') {
            steps {
                //python3 Hello.py
                python3 --version
            }
        }
    }
}