from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def greet(name: str = 'Recruto', message: str = 'Давай дружить'):
    return f"<h1> Hello {name}! {message}!</h1>"

if __name__ == '__main__':
    uvicorn.run('main:app')

