# from flask import Flask,request

# app = Flask(__name__)

# @app.route("/soma", methods=['POST'])
# def soma():
#     args=request.get_json()
#     print(args)
#     x=args['x']
#     y=args['y']
#     resultado=x+y
#     data = {"resultado": x+y}
#     return data
# if __name__ == '__main__':
#     app.run(app.run(port=5000, host='0.0.0.0', debug=True))

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Soma(BaseModel):
    x: int
    y: int

@app.post("/soma")
async def soma(item: Soma):
    x = item.x
    y = item.y
    soma = x+y
    return {"resultado" : soma}

@app.post("/subtracao")
async def sub(item: Soma):
    x = item.x
    y = item.y
    soma = x-y
    return {"resultado" : soma}

uvicorn.run(app, host="0.0.0.0", port="5000")