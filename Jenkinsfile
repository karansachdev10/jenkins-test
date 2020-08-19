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
				sh 'sudo ssh -i /home/ec2-user/karan_kp.pem ec2-user@54.90.32.103'
			}
		}
		
	}
}
