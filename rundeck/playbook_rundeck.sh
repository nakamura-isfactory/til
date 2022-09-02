#!/bin/bash

time ansible-playbook -i hosts rundeck.yml ; echo ES $?
sudo cat /tmp/install_rundeck.txt
