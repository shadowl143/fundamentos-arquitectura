# sync_app.py -- WSGI
import time
import asyncio
from flask import Flask
app = Flask(__name__)

@app.get("/lento")
def lento():
    time.sleep(0.5) # espera BLOQUEANTE
    return {"ok": True}

# async_app.py -- ASGI
from fastapi import FastAPI
app = FastAPI()

@app.get("/lento/asgi")
async def lento():
    await asyncio.sleep(0.5) # espera NO bloqueante
    return {"ok": True}