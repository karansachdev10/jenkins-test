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
				sh 'pip install pylint'
			}
		}
		stage('Test') {
			steps {
				echo "Testing"
				sh 'pylint app.py'
				sh 'python test.py'
			}
		}
		stage('Deploy') {
			steps {
				sh 'sudo scp -i /home/ec2-user/karan_kp.pem -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/jenkins-test ec2-user@54.90.32.103:/tmp'
			}
		}
		
	}
}
