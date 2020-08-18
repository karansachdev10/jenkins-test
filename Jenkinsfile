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
				sh 'python3 test.py'
			}
		}
	}
}
