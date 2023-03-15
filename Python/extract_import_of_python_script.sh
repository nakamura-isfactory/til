#!/usr/bin/bash
#:description:Pythonスクリプトからimport文だけを抽出する。

function extract_import_of_python_script() {
  find -type f -name '*.py' | xargs grep -h ^import
  find -type f -name '*.py' | xargs grep -h ^from.*import
}

extract_import_of_python_script | tr -d '\r' | sort -u | uniq
