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
        }          
     }
  }
}
     

