pipeline {
    agent any

    stages {
        stage("Testing code") {
            steps {
                echo "Running mypy"
                sh "mypy ."
            }
        }
        stage("Running Pylint") {
            steps {
                sh "pylint mypy_validation.py"
            }
        }
    }
}