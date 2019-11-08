pipeline {
	agent {
		docker {
			image "python:3.7.2"
			args "-u root"
		}
	}
	stages {
		stage ("Build - Setup Requirements"){
			steps {
			    echo "$USER $HOME"
				sh "pip install -r requirements.txt"
			}
		}
		stage ("Test - Unittest") {
			steps {
				sh "python -m unittest discover tests"
			}
		}
	}
}