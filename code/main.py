from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import JSONResponse, HTMLResponse

from code import database, dependencies
from code.users import routers as user_routers

app = FastAPI()
app.include_router(user_routers.router)
app.state.database = database.database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

    await dependencies.Connection.close_redis()


@app.get("/hello/")
async def hello(request: Request):
    redis = dependencies.Connection.redis()
    await redis.setex('surname', 10, 'abay')
    return {'surname': await redis.get('surname')}
    # i should learn redis commands and pipelines in redis and i should learn redis library


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:9000/websocket");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/chat/")
async def chat():
    return HTMLResponse(html)


@app.websocket("/websocket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
