from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world!"}

@app.get("/method")
def read_item():
    return {"method": "GET"}

@app.put("/method")
def put_item():
    return {"method": "PUT"}

@app.options("/method")
def met_info():
    return {"method": "OPTIONS"}

@app.delete("/method")
def deleting_stuff():
    return {"method": "DELETE"}

@app.post("/method")
def post_item():
    return {"method": "POST"}

@app.post("/method", status_code=201)
async def post_item():
    return {"method": "POST"}