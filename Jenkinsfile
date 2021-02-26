#!/usr/bin/env groovy 

pipeline {
  agent any
  triggers {
    cron('0 * * * *')
  }
  options{
    quietPeriod(30) //Quiet period in seconds
  }
  stages{
    stage('Run script'){
      steps{
              sh "python greetings.py"
<<<<<<< HEAD:jenkinsfile
            }          
      }
  }
       
=======
        }          
    }
>>>>>>> 223619cd53f8455189504e96bf59070b1350679a:Jenkinsfile
}
