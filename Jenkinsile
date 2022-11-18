pipeline {
    agent any

    environment{
		PYTHON_PATH = "C:\\Users\\Student\\AppData\\Local\\Programs\\Python\\Python310"
    }
    stages {
        stage('Build') {
            steps {
                echo "Building..."
                bat "${env.PYTHON_PATH}\\python.exe -v"
            }
        }
        stage('Tests') {
            steps {
                bat "${env.PYTHON_PATH}\\Scripts\\py.test.exe main.py"
            }
        }
        stage('Deploy') {
            steps {
                bat "${env.PYTHON_PATH}\\python.exe main.py"
            }
        }
    }
}