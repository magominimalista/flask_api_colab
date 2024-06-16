import pandas as pd
from openpyxl import load_workbook
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import nest_asyncio
from pyngrok import ngrok
import uvicorn

app = FastAPI()


async def load_data():
    wb = load_workbook('dados.xlsx')
    ws = wb.active
    data = pd.DataFrame(ws.values)
    data.columns = data.iloc[0]
    data = data.iloc[1:].fillna('')
    return data.to_dict(orient='records')


@app.get("/data")
async def get_data():
    data = await load_data()
    return JSONResponse(content=data)


@app.get('/index')
async def home():
    return "Hello World"

ngrok.set_auth_token("2hyHyJYYQrBLUz6qBvxHDSCIv9I_5UdbRCw4oK4NSb8xf7qec")

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
