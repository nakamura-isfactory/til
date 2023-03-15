all: version/python-multipart.txt \
		version/pytest.txt \
		version/SQLAlchemy.txt \
		version/alembic.txt \
		version/deptree.txt

version:
	mkdir -p version
	chmod +x *.sh

version/pyenv.txt:
	make version
	./install_pyenv.sh
	( pyenv version ; date ) | tee $@

version/python311.txt: version/pyenv.txt
	echo "API サーバプログラム実行用に Python 3.11 をインストールする。"
	make version
	EXPECTED_PYTHON_VERSION=3.11.2 bash -uex ./install_python.sh
	( echo make $@ ; python -V ; date ) | tee $@
	pip freeze > requirements_python311.txt

version/python-dotenv.txt: version/python311.txt
	echo "https://qiita.com/harukikaneko/items/b004048f8d1eca44cba9"
	make version
	pip install python-dotenv
	( echo make $@ ; pip show python-dotenv ; date ) | tee $@

version/fastapi.txt: version/python311.txt
	make version
	pip3 install "fastapi[all]"
	pip3 freeze > requirements_fastapi.txt
	( echo make $@ ; grep '^fastapi' requirements_fastapi.txt ; date ) | tee $@

version/python-multipart.txt: version/fastapi.txt
	make version
	echo "https://fastapi.tiangolo.com/ja/tutorial/request-files/"
	echo "To receive uploaded files, first install python-multipart."
	pip3 freeze > requirements_fastapi.txt
	pip3 install python-multipart
	( echo make $@ ; grep '^python-multipart' requirements_fastapi.txt ; date ) | tee $@

version/pytest.txt: version/python311.txt
	make version
	pip3 install "pytest"
	pip3 freeze > requirements_fastapi.txt
	( echo make $@ ; grep '^pytest' requirements_fastapi.txt ; date ) | tee $@

version/mysql-connector-python.txt: version/python311.txt
	make version
	echo "https://qiita.com/IKEH/items/0211bf81b16c15bed1e2"
	pip3 install "mysql-connector-python"
	pip3 freeze > requirements_fastapi.txt
	( echo make $@ ; grep '^mysql-connector-python' requirements_fastapi.txt ; date ) | tee $@

version/SQLAlchemy.txt: version/mysql-connector-python.txt
	make version
	echo "https://docs.sqlalchemy.org/en/20/intro.html#installation"
	pip3 install "SQLAlchemy"
	pip3 freeze > requirements_fastapi.txt
	( echo make $@ ; grep '^SQLAlchemy' requirements_fastapi.txt ; date ) | tee $@

version/alembic.txt: version/mysql-connector-python.txt
	make version
	echo "https://qiita.com/ktamido/items/8c3e56de1e889ec8a4cf"
	echo "https://alembic.sqlalchemy.org/en/latest/tutorial.html"
	pip3 install "alembic"
	pip3 freeze > requirements_fastapi.txt
	( echo make $@ ; grep '^alembic' requirements_fastapi.txt ; date ) | tee $@

version/deptree.txt: version/python311.txt
	echo "パッケージの依存関係を調べるツール deptree をインストールする。"
	make version
	echo "https://pypi.org/project/deptree/"
	pip3 install "deptree"
	pip3 freeze > requirements_deptree.txt
	( echo make $@ ; grep '^deptree' requirements_deptree.txt ; date ) | tee $@
