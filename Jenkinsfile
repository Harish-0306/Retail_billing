
pipeline {
    agent any

    environment {
        APP_DIR = "~/retail_app"
        SSH_TEST = "test-ec2-ssh"
        SSH_PROD = "prod-ec2-ssh"
        TEST_IP = "65.2.63.246"     // Replace with test EC2 IP
        PROD_IP = "65.2.63.246"     // Replace with prod EC2 IP
    }

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/Harish-0306/Retail_billing.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh './venv/bin/python3 -m unittest discover -s tests'
            }
        }

        stage('Deploy to Test') {
            steps {
                sshagent (credentials: [env.SSH_TEST]) {
                    sh '''
                    ssh ec2-user@$TEST_IP "
                        pkill -f app.py || true
                        mkdir -p $APP_DIR
                        cd $APP_DIR
                        git clone https://github.com/your-username/your-repo.git . || git pull
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                        nohup python3 app.py > output.log 2>&1 &
                    "
                    '''
                }
            }
        }

        stage('Deploy to Production') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                sshagent (credentials: [env.SSH_PROD]) {
                    sh '''
                    ssh ec2-user@$PROD_IP "
                        pkill -f app.py || true
                        mkdir -p $APP_DIR
                        cd $APP_DIR
                        git clone https://github.com/your-username/your-repo.git . || git pull
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                        nohup python3 app.py > output.log 2>&1 &
                    "
                    '''
                }
            }
        }
    }
}
