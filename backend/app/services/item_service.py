from sqlalchemy.orm import Session
from app.db.models.item import Item
from app.schemas.item import ItemCreate

def create_item(db: Session, item: ItemCreate, user_id: int):
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
