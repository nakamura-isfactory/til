#!/usr/bin/bash

function load_average_1() {
  uptime | awk '{ print $10 }' | sed -e 's/,//'
}

PS1="exit_status=\$?\nload_average_1=\$(load_average_1)\n[\u@\h \W]\$ "
