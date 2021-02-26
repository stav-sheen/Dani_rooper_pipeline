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
    stage('install requests if not available'){
      steps{
              sh "pip install requests"
        }          
    }
    stage('Run weather script'){
      steps{
              sh "python weather.py ${OMW_API_KEY}"
        }          
     }
  }
}
     

