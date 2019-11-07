pipeline {
	agent {
		docker {
			image 'python 3.7.2'
		}
	}
	stages {
		stage ('Build - Setup Requirements'){
			steps {
				sh 'sudo pip install -r requirements.txt'
			}
		}
		stage ('Test') {
			steps {
				sh 'sudo python -m unittest discover tests'
			}
		}
	}
}