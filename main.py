from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/method")
def read_root():
    return {"method": "GET"}