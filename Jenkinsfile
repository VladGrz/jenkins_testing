pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'Lab_2', url: 'https://github.com/VladGrz/DDICN_Labs.git'
            }
        }
        
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