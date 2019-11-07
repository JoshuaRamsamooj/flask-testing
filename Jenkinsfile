pipeline {
	agent {
		docker {
			image "python:3.7.2"
		}
	}
	stages {
		stage ("Build - Setup Requirements"){
			steps {
			    echo "$USER"
				sh "sudo --user pi pip install -r requirements.txt"
			}
		}
		stage ("Test - Unittest") {
			steps {
				sh "python -m unittest discover tests"
			}
		}
	}
}