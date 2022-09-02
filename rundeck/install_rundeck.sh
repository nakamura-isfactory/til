#!/bin/bash -x

pwd
curl https://raw.githubusercontent.com/rundeck/packaging/main/scripts/rpm-setup.sh 2> /dev/null | sudo bash -s rundeck
ls -l /etc/yum.repos.d/rundeck.repo
sudo yum install -y rundeck
