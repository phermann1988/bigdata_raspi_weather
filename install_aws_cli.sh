#!/bin/bash
# w/ aws cli you can communicate w/ your aws account from the command line
# to use this you will need: AWS account + IAM role (w/ programmatic access for iot)
# AWS account: https://www.youtube.com/watch?v=uJssXPyMf0s
# IAM example : https://www.youtube.com/watch?v=DXNS-EP9sXM
#you need to have python3 + pip installed on your os but should be by default..
sudo pip install awscli
complete -C aws_completer aws

#at this point you will need the credentials of the IAM role / iot user
#check your region at aws web gui console (upper right corner):
#https://docs.aws.amazon.com/de_de/general/latest/gr/rande.html
aws configure
