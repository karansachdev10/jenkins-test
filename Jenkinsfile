pipeline {
	agent {
		docker {
			image 'python3.7'
		}
	}
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
	}
}
