# FastAPI application entry point file
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/health')
def read_health():
    return {'status': 'healthy'}