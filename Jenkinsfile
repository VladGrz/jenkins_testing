pipeline {
    agent any

    stages {
        stage("Installation") {
            steps {
                echo "Installing all required modules"
                sh "sudo apt-get update"
                sh "sudo apt install pip"
                sh "pip install mypy"
                sh "sudo apt install mypy"
            }
        }
        stage("Testing code") {
            echo "Running mypy"
            sh "mypy ."
        }
    }
}