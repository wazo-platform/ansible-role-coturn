pipeline {

  agent {
    label 'molecule-aws'
  }

  stages {

    stage ('Test') {
      steps {
        script { checkout scm }
        sh 'tox'
      }
    }

  }

}
