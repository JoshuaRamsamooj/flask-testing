pipeline {
	agent any
	stages {
		stage ('Build - Setup Requirements'){
			steps {
				sh 'pip3 install -r requirements.txt'
			}
		}
		stage ('Test') {
			steps {
				sh 'python3 -m unittest discover tests'
			}
		}
	}
}