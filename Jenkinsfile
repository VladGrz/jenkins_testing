pipeline {
    agent any

    stages {
        stage("Testing code") {
            steps {
                echo "Running mypy"
                sh "mypy ."
            }
        }
    }
}