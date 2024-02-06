from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from loguru import logger

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
            if request.is_disconnected():
                logger.warning("Client has ended the connection.")
                break

            yield {
                "license_plate": "A123BC",
                "reason": "Status should be 'Used in 1c', not Weighted.",
            }
            asyncio.sleep(5)

    return EventSourceResponse(generator())

@app.get("/feecc-barrier-logic/force-open")
def force_open() -> Response:
    return Response(status_code=200)