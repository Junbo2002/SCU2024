from fastapi import Depends, FastAPI

# from .dependencies import get_query_token, get_token_header
# from .internal import admin
from backend.routers import tracks, rec

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

app.include_router(tracks.router)
app.include_router(rec.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="172.16.0.25", port=8000,)