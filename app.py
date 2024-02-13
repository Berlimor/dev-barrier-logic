from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from loguru import logger
import random

import asyncio


app = FastAPI(title="Feecc-barrier-logic")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PATCH", "DELETE", "PUT"],
    allow_headers=["*"],
)


@app.get("/feecc-barrier-logic/stream")
async def stream_status(request: Request) -> EventSourceResponse:
    async def generator():
        while True:
            if await request.is_disconnected():
                logger.warning("Client has ended the connection.")
                break
            num = round(random.random()*1000)
            yield {
                "data": {
                    "license_plate": f"A{num}BC",
                    "reason": "Статус авто должен быть <Used in 1c>, а не <Weighted>",
                }
            }

            await asyncio.sleep(5)

    return EventSourceResponse(generator())

@app.get("/feecc-barrier-logic/force-open")
def force_open() -> Response:
    return Response(status_code=200)