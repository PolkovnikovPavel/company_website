from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import *
import os


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"))


@app.get("/{file_path:path}")
async def get_likely_place(file_path: str):
    if '.html' in file_path:
        file_path = file_path.replace('.html', '')

    if os.path.exists(f'templates/{file_path}.html'):
        return FileResponse(f'templates/{file_path}.html')
    return FileResponse(f'templates/index.html')


app.mount("/", StaticFiles(directory="templates", html=True))
