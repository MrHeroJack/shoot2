from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# 确保导入 CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas # . 代表当前目录
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 定义允许的来源
# 常见的 Vue CLI 开发服务器端口是 8080、8081 等。
# 常见的 Vite 开发服务器端口是 5173、3000 等。
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:8081", # 万一 8080 端口被占用
    "http://127.0.0.1:8081",
    "http://localhost:5173", # Vite 的默认端口
    "http://127.0.0.1:5173",
    # 如果需要，添加其他来源，例如您部署的前端 URL
]

# 添加 CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许特定的来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法 (GET, POST 等)
    allow_headers=["*"],  # 允许所有请求头
)

@app.post("/items/", response_model=schemas.Item)
def create_item_endpoint(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/items/", response_model=List[schemas.Item])
def read_items_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="项目未找到") # 项目未找到
    return db_item

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item_endpoint(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="项目未找到") # 项目未找到
    return db_item

@app.delete("/items/{item_id}", response_model=schemas.Item) # 或者 response_model=None 或一些状态消息
def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None: # 如果 delete_item 在未找到项目时返回 None (或在删除前检查)
         pass # 即使未找到项目也返回 204 或适当的响应，如果项目必须存在则返回 404
    # 考虑返回什么。FastAPI 默认为 JSON，因此返回已删除的项目是常见的做法，
    # 或者返回状态消息。如果 crud.delete_item 现在返回已删除的项目 (或 None)，则这样可以。
    # 如果它不返回项目 (例如仅状态)，则调整 response_model 或返回一个 Response。
    # 目前，假设 crud.delete_item 返回已删除的项目，如果未找到则返回 None。
    # 为了确保始终返回 200 OK 及项目，或 404，我们应确保 crud.delete_item
    # 要么引发错误，要么一致地返回项目。
    # 我们来调整一下，简单地返回成功消息或项目。
    # 在此示例中，我们假设 crud.delete_item 返回已删除的项目。
    # 如果 crud.delete_item 因未找到而返回 None，我们应该引发 404。
    # 当前的 crud.delete_item 返回 db_item (如果在删除尝试前未找到，则可能为 None)
    # 一个更好的 crud.delete_item 实现方式是：
    #   db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    #   if not db_item: return None
    #   db.delete(db_item)
    #   db.commit()
    #   return db_item
    # 鉴于当前的 crud.delete_item：
    deleted_item_info = crud.get_item(db, item_id) # 重新获取以确认或获取数据（如果删除操作未返回数据）
                                                   # 这并不理想，crud.delete_item 应该返回项目或指示未找到的信号
                                                   # 我们假设 crud.delete_item 确实返回项目或 None
    # 提供的 crud.delete_item 在找到项目的情况下，返回删除前的项目对象，否则返回 None。
    # 这意味着如果找到了并删除了，db_item 就是该对象。如果未找到，则为 None。
    if db_item is None:
         raise HTTPException(status_code=404, detail="项目未找到") # 项目未找到
    return db_item # 返回被删除的项目

@app.get("/")
def read_root():
    return {"你好": "世界"} # {"你好": "世界"}

# 注意：CORS 中间件将在后续的集成步骤中添加。
