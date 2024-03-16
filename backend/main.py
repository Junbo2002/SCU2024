from fastapi import Depends, FastAPI

# from .internal import admin
from backend.routers import req, rec, visualize
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# =================
# 添加路由
# =================

# 调用lastfm官方接口
app.include_router(req.router)

# 推荐接口
app.include_router(rec.router)

# 数据可视化接口
app.include_router(visualize.router)

# 静态文件映射
app.mount("/static", StaticFiles(directory="assets"), name="static")

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
    return {"message": "Hello MIR!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="172.16.0.50", port=8000)