#!/usr/bin/bash -ue

echo "前提: pyenv をインストールして使用可能にしてある。"
which pyenv
pyenv version

echo EXPECTED_PYTHON_VERSION is "${EXPECTED_PYTHON_VERSION:?}"

#:Python インストールの事前準備
#:https://qiita.com/daikumatan/items/64cd6bd566460f57f618
sudo yum install -y git
sudo yum install -y zlib-devel
echo "openssl-devel と openssl-devel11 両方インストールしようとすると conflicts する。どちらか1つだけにする。"
#:sudo yum install -y openssl-devel
sudo yum install -y sqlite-devel.x86_64
sudo yum install -y xz-devel
sudo yum install -y tree

#:https://aifx.tech/centos7-python/
#:Python インストールの事前準備
sudo yum remove -y openssl-devel
sudo yum groupinstall -y "development tools"
sudo yum install -y bzip2-devel gdbm-devel libffi-devel libuuid-devel \
  ncurses-devel openssl11 openssl11-devel readline-devel sqlite-devel xz-devel \
  zlib-devel

if pyenv install --list | grep "${EXPECTED_PYTHON_VERSION}" ; then
    pyenv install "${EXPECTED_PYTHON_VERSION}"
    pyenv global "${EXPECTED_PYTHON_VERSION}"
    pyenv versions
fi

if [ -d ~/.pyenv/shims ]; then
    if ! grep -q /.pyenv/shims ~/.bash_profile ; then
        ( echo 'PATH=~/.pyenv/shims:$PATH' ; echo "export PATH" ) >> ~/.bash_profile
        set +u
        . ~/.bash_profile
        set -u
    fi
fi
echo PATH is $PATH

which python
which python3
#:when executed EXPECTED_PYTHON_VERSION=3.11.2 ./install_python.sh
#:~/.pyenv/shims/python
#:when executed EXPECTED_PYTHON_VERSION=3.9.7 ./install_python.sh
#:~/.pyenv/shims/python

python3 -VV
python -VV
#:when executed EXPECTED_PYTHON_VERSION=3.11.2 ./install_python.sh
#:Python 3.11.2 (main, Feb 15 2023, 08:15:24) [GCC 7.3.1 20180712 (Red Hat 7.3.1-15)]
#:when executed EXPECTED_PYTHON_VERSION=3.9.7 ./install_python.sh
#:Python 3.9.7 (default, Mar  2 2023, 02:57:05) 

pip3 --version
pip --version
#:when executed EXPECTED_PYTHON_VERSION=3.11.2 ./install_python.sh
#:pip 22.3.1 from /home/ec2-user/.pyenv/versions/3.11.2/lib/python3.11/site-packages/pip (python 3.11)
#:when executed EXPECTED_PYTHON_VERSION=3.9.7 ./install_python.sh
#:pip 21.2.3 from /home/ec2-user/.pyenv/versions/3.9.7/lib/python3.9/site-packages/pip (python 3.9)
