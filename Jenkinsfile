pipeline {
	agent any
    	stages {
		stage('Clean code') {
        			steps {
					echo "Cleaning code"
            				step([$class: 'WsCleanup'])
        			}
    		}

		stage('Checkout code') {
        			steps {
					echo "Checking out now"
            				checkout scm
        			}
    		}
		stage('Build') {
			steps {
				echo "Building"
				sh 'python3 -m venv venv'
				sh 'source venv/bin/activate'
			}
		}
		stage('Test') {
			steps {
				echo "Testing"
				sh 'python test.py'
			}
		}
		stage('Deploy') {
			steps {
				echo "Deploying"
				sh 'sudo scp -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/jenkins-test/app.py ec2-user@54.90.32.103:/home/ec2-user/jenkins-test@tmp'
				sh 'sudo ssh -i /home/ec2-user/karan_kp.pem ec2-user@54.90.32.103'
				sh 'sudo yum install python3'
				sh 'python3 -m venv venv'
				sh 'source venv/bin/activate'
				sh 'python3 app.py'
			}
		}
		
	}
}
