pipeline {
    agent any

    stages {
        stage("Installation") {
            steps {
                echo "Installing all required modules"
                sh "apt-get update"
                sh "apt install pip"
                sh "pip install mypy"
                sh "apt install mypy"
            }
        }
        stage("Testing code") {
            steps {
                echo "Running mypy"
                sh "mypy ."
            }
        }
    }
}