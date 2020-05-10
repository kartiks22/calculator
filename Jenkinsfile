pipeline {
    environment {
        registry = "kartiks22/calculator"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Build') {
            steps{
                script {
                    dockerImage = docker.build registry + ":latest"
                }
            }
        }
        stage('test'){
            steps {
                sh 'pip3 install pytest'
                sh 'pytest'
            }
        }
        stage('Archive'){
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                build 'rundeck_deploy'
            }
        }
    }
}

/*pipeline {
    environment {
        dockerImage = ''
    }
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'ls'
                sh 'curl -H "Content-Type: application/json" --data "{"build": true}" -X POST https://registry.hub.docker.com/u/kartiks22/calculator/trigger/57317c28-14ae-407a-b01b-7503a7693749/'
            }
        }
        stage('test'){
            steps {
                sh 'pip3 install pytest'
                sh 'pytest'
            }
        }
        stage('Archive'){
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                    }
                }
            }
        }       
        stage('Deploy') {
            steps {
                build 'rundeck_deploy'
            }
        }
    }
}*/
