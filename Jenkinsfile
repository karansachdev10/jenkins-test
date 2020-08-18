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
		stage('Test') {
			steps {
				sh "pytest test.py"
			}
		}
	}
}
