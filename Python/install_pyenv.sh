#!/usr/bin/bash -ue
which git
echo "read https://github.com/pyenv/pyenv#basic-github-checkout"
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
#:Optionally, try to compile a dynamic Bash extension to speed up Pyenv. 
#:Don't worry if it fails; Pyenv will still work normally:
cd ~/.pyenv && src/configure && make -C src || :
if ! grep -q pyenv ~/.bash_profile ; then
    ( echo 'PATH=$PATH:~/.pyenv/bin' ; echo "export PATH" ) >> ~/.bash_profile
    . ~/.bash_profile
fi
which pyenv
#:expected:~/.pyenv/bin/pyenv
pyenv --version
#:expected:pyenv 2.3.12-16-gc8daaa39
pyenv install --list | grep "^ *3" | tail -n 22
#:expected:3.9.16, 3.10.0, ..., 3.11.2
