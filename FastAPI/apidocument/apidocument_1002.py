#!python3
# :basenaem:apidocument_1002.py
# :https://fastapi.tiangolo.com/ja/tutorial/response-model/
# :$ make version/fastapi.txt
# :$ make version/python-multipart.txt

from typing import Optional
import logging
import os
import shutil
from fastapi import (
  FastAPI, 
  File, 
  UploadFile, 
  Form
)
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# class ProjectAddRequestBody(BaseModel):
#   theme_selection: str
#   base_theme_url: str
#   base_theme_id_1: str
#   base_theme_id_2: str
#   template_id: str
#   dummy_int: int

class Project(BaseModel):
  project_id: int

@app.post(
    "/users/{userId}/projects/add",
    summary="ファイルをインポートしないでプロジェクトを作成する",
    description="ファイルをインポートしないでテーマ、テンプレートを指定してプロジェクトを作成する",
    response_model=Project,
    responses={
        200: {
            "content": {"application/xml": {}},
            "description": "Return the JSON item or an image.",
        }
    },
)
async def create_project(
    userId: int,
    theme_selection: str = Form(),
    base_theme_url: Optional[str] = Form(None),
    base_theme_id_1: str = Form(),
    base_theme_id_2: str = Form(),
    template_id: str = Form(),
    dummy_int: str = Form()
):
  return {"project_id": "123456"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
