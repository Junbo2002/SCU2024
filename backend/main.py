from fastapi import Depends, FastAPI

# from .dependencies import get_query_token, get_token_header
# from .internal import admin
from backend.routers import tracks, rec, visualize
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

# 添加路由
app.include_router(tracks.router)
app.include_router(rec.router)
app.include_router(visualize.router)

# 静态文件映射
app.mount("/static", StaticFiles(directory="assets"), name="static")
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )

# 解决跨域问题
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="172.16.0.49", port=8000)