# sync_app.py -- WSGI
import time
from flask import Flask
app = Flask(__name__)

@app.get("/lento")
def lento():
    time.sleep(0.5) # espera BLOQUEANTE
    return {"ok": True}

# async_app.py -- ASGI
import asyncio
from fastapi import FastAPI
app = FastAPI()

@app.get("/lento")
async def lento():
    await asyncio.sleep(0.5) # espera NO bloqueante
    return {"ok": True}