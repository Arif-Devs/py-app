pipeline {
    agent {
        label 'ec2-slave'
    }

    stages {
        stage('Deployment'){
            steps{
                sh 'docker pull arif164/pyappimage'
                sh 'docker rm -f webos1'
                sh 'docker run -dit --name webos1 -p 80:80 arif164/pyappimage'
            }
        }
    }
}
