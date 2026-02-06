pipeline {
    agent {
        label 'ec2'
    }

    stages {
        stage('Deployment'){
            steps{
                sh 'docker pull jinny1/gfgdevops30'
                sh 'docker rm -f webos1'
                sh 'docker run -dit --name webos1 -p 80:80 jinny1/gfgdevops30'
            }
        }
    }
}
