pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/Harish-0306/Retail_billing.git' // Replace with your actual repo
            }
        }

        stage('Set Up Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh './venv/bin/python3 -m unittest discover -s tests'
            }
        }
    }
}
