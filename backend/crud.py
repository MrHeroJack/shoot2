from sqlalchemy.orm import Session
from . import models, schemas

def get_item(db: Session, item_id: int):
    """根据 ID 获取单个物品。"""
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    """获取物品列表，支持分页。"""
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    """创建一个新物品。"""
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    """根据 ID 更新现有物品。"""
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.description = item.description
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    """根据 ID 删除物品。"""
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
