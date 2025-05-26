from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Make sure to import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas # . represents current directory
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Define allowed origins
# Common Vue CLI dev server ports are 8080, 8081 etc.
# Common Vite dev server ports are 5173, 3000 etc.
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:8081", # In case 8080 is taken
    "http://127.0.0.1:8081",
    "http://localhost:5173", # Default for Vite
    "http://127.0.0.1:5173",
    # Add other origins if needed, e.g., your deployed frontend URL
]

# Add CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
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
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item_endpoint(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}", response_model=schemas.Item) # or response_model=None or some status message
def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None: # If delete_item returns None when not found (or check before delete)
         pass # Return a 204 or appropriate response even if item not found, or 404 if it must exist
    # Consider what to return. FastAPI default is JSON, so returning the deleted item is common,
    # or a status message. If crud.delete_item now returns the deleted item (or None), this is fine.
    # If it doesn't return the item (e.g. just status), adjust response_model or return a Response.
    # For now, assuming crud.delete_item returns the deleted item or None if not found.
    # To make it always return a 200 OK with the item or 404, we should ensure crud.delete_item
    # either raises an error or returns the item consistently.
    # Let's adjust to simply return a success message or the item.
    # For this example, we'll assume crud.delete_item returns the item that was deleted.
    # If crud.delete_item returns None because it wasn't found, we should raise 404.
    # The current crud.delete_item returns the db_item (which could be None if not found before delete attempt)
    # A better crud.delete_item would be:
    #   db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    #   if not db_item: return None
    #   db.delete(db_item)
    #   db.commit()
    #   return db_item
    # Given the current crud.delete_item:
    deleted_item_info = crud.get_item(db, item_id) # Re-fetch to confirm or get data if not returned by delete
                                                   # This is not ideal, crud.delete_item should return the item or signal not found
                                                   # Let's assume crud.delete_item actually returns the item or None
    # The crud.delete_item provided returns the item object *before* it's deleted if found, or None.
    # This means if it was found and deleted, db_item is the object. If not found, it's None.
    if db_item is None:
         raise HTTPException(status_code=404, detail="Item not found")
    return db_item # Return the item that was deleted

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Note: CORS middleware will be added later in the integration step.
