pipeline {
	agent any
    	stages {
		stage('Clean code') {
        			steps {
            				step([$class: 'WsCleanup'])
        			}
    		}

		stage('Checkout code') {
        			steps {
            				checkout scm
        			}
    		}
		stage('Build') {
			steps {
				sh 'python3 -m venv venv'
				sh 'source venv/bin/activate'
			}
		}
		stage('Test') {
			steps {
				sh 'sudo pip3 install pytest'
				sh 'sudo pytest test.py'
			}
		}
	}
}
