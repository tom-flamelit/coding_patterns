from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from model import Counter

app = FastAPI()
counter = Counter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/add1")
async def add_one():
    old_value = counter.get_value()
    new_value = counter.add_one()  # This will automatically read the latest value and save the new one
    return JSONResponse(content={"new_value": new_value,"old_value":old_value})

@app.get("/subtract1")
async def subtract_one():
    old_value = counter.get_value()
    new_value = counter.subtract_one()  # As above
    return JSONResponse(content={"new_value": new_value, "old_value":old_value})

@app.get("/report")
async def report():
    current_value = counter.get_value()  # Reads the current value
    return JSONResponse(content={"current_value": current_value})
