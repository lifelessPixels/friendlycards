import asyncio
import websockets
import pathlib
import ssl
from gamepool import GamePool
from lobby import Lobby
from enums import ConnectionState, RequestStatus

game_pool = GamePool()

async def server_job(sock, path):

    # client connected, do something with it 
    client_state = ConnectionState.CONNECTED
    while client_state != ConnectionState.DISCONNECTED:
        try:
            json_data = await sock.recv()
            status = game_pool.client_request(sock.remote_address, json_data)
            await sock.send(status[1])

        except websockets.ConnectionClosed:
            game_pool.client_disconnected(sock.remote_address)
            client_state = ConnectionState.DISCONNECTED

start_server = websockets.serve(server_job, "0.0.0.0", "6789")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

'''

ws = new WebSocket("ws://localhost:6789")
ws.onmessage = function (event) {
    console.log(event.data)
}
ws.send("data")

'''