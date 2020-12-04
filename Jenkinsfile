pipeline {

  agent any

  stages {

    stage ('Test') {
      steps {
        script { checkout scm }
        sh 'tox'
      }
    }

  }

}
