pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'ls'
                sh 'curl -H "Content-Type: application/json" --data "{"build": true}" -X POST https://registry.hub.docker.com/u/kartiks22/calculator/trigger/57317c28-14ae-407a-b01b-7503a7693749/'
            }
        }
        // stage('test'){
        //     steps {
        //         sh 'pip3 install pytest'
        //         sh 'pytest'
        //     }
        // }
        // stage('Deploy') {
        //     steps {
        //         build 'Rundeck_deploy'
        //     }
        // }
    }
}
