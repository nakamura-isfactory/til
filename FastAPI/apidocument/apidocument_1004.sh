#!/usr/bin/bash
#:basename:apidocument_1004.sh
echo "http://127.0.0.1:11004/"
echo "http://127.0.0.1:11004/docs"
uvicorn apidocument_1004:app --reload --port 11004
