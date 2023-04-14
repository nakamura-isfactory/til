import secrets
import logging
from logging import StreamHandler
import os
from dotenv import load_dotenv
from typing import Annotated
from fastapi import FastAPI
from fastapi import File
from fastapi import Depends
from fastapi import UploadFile
from fastapi import HTTPException
from fastapi import Query
from fastapi import status
from fastapi.responses import FileResponse
import uvicorn
import uuid
from text_data import post_text_data

description = """xxx
"""

app = FastAPI(
    title="APIサーバ",
    description=description,
    version="0.0.1"
)
logger = logging.getLogger("uvicorn")
handler = StreamHandler()
logger.addHandler(handler)
responses = {
    408: {"description": "Request Timeout"},
}


@app.post("/create_text_data_2",
          responses={**responses,
                     200: {"content": {"application/octet-stream": {}},
                           "description": "《テキストデータ》"}},
          response_class=FileResponse
          )
def create_text_data_2(
    contents: UploadFile = Query(description="《コンテンツ》"), 
    contents_1: UploadFile = None,
    contents_2: Annotated[
        list[UploadFile], File(description="《コンテンツ》")
    ] = None,
    contents_3: Annotated[
        UploadFile, File(description="《コンテンツ》")
    ] = None
):
    logger.info('create_text_data_2 begin')
    logger.info('create_text_data_2 end')
    return FileResponse('/tmp/dummy.txt')
    

@app.post("/create_text_data",
          responses={**responses,
                     200: {"content": {"application/octet-stream": {}},
                           "description": "《テキストデータ》"}},
          response_class=FileResponse
          )
def create_text_data(
    contents: Annotated[
        UploadFile, File(description="《コンテンツ》")
    ],
    check_image: bool = Query(
        False, description="《リソース指定》")
):
    """xxx
    """
    logger.info('create_text_data begin')
    logger.info('create_text_data end')
    return FileResponse('/tmp/dummy.txt')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
