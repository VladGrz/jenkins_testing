pipeline {
    agent any

    options { skipDefaultCheckout() }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'vhrozovsky/mypy_testing', url: 'https://github.com/VladGrz/jenkins_testing.git'
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