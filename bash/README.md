1. prompt.sh をホームディレクトリに置く。
2. $ vi ~/bash_profile
3. 末尾に追記する。

if [ -f ~/prompt.sh ]; then
	. ~/prompt.sh
fi

4. . ~/bash_profile
