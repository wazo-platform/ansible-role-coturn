pipeline {
  agent none
  stages {
    stage ('Lint') {
      agent {
        label 'molecule-aws-amd64-debian13-small'
      }
      steps {
        checkout scm
        sh 'tox -e linters'
      }
      post {
        always {
          cleanWs()
        }
      }
    }
    stage ('Test') {
      parallel {
        stage ('Debian 11 / Ansible 8') {
          agent {
            label 'molecule-aws-amd64-debian12-small'
          }
          steps {
            checkout scm
            sh 'tox -e molecule-ansible8'
          }
          post {
            always {
              cleanWs()
            }
          }
        }
        stage ('Debian 13 / Ansible 13') {
          agent {
            label 'molecule-aws-amd64-debian13-small'
          }
          steps {
            checkout scm
            sh 'tox -e molecule-ansible13'
          }
          post {
            always {
              cleanWs()
            }
          }
        }
      }
    }
  }
}
