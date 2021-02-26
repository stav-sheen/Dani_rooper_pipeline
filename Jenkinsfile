#!/usr/bin/env groovy 

pipeline {
  agent any
  triggers {
    cron('* * * * *')
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
     

