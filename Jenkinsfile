pipeline {

  agent {
    label 'molecule'
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
