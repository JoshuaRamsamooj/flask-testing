pipeline {
	agent {
		docker {
			image 'python 3.7.2'
		}
	}
	stages {
		stage ('Build - Setup Requirements'){
			steps {
				sh 'pip install -r requirements.txt'
			}
		}
		stage ('Test') {
			steps {
				sh 'python -m unittest discover tests'
			}
		}
	}
}