from fastapi import FastAPI
from allindices import *

app = FastAPI()

@app.get("/")
def read_root():
    list = handl_all_indices()

    return list