import bcrypt


from fastapi import Body, FastAPI, Response, status, Depends, HTTPException, Security, Header, Request
from sqlalchemy.orm import Session
import models
from fastapi.middleware.cors import CORSMiddleware


from database import engine, get_db
import schemas
import utils

import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


app = FastAPI()


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

# pwd_context = CryptContext(schemes=['bcrypt'])
models.Base.metadata.create_all(bind=engine)

# db: Session = Depends(get_db) (pass in to routes when doing sql stuff)


@app.get("/words")
def send_words():
    return "hello"


@app.get("/spells/", response_model=list[schemas.Spell],
         )
def read_spells(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    spells = utils.get_spells(db, skip=skip, limit=limit)
    return spells


@app.get("/spells/{spell_name}", response_model=schemas.Spell)
def get_spell(spell_name: str, db: Session = Depends(get_db),):
    spell = utils.get_spell_by_name(db, spell_name)
    return spell


@app.post("/spells/", response_model=schemas.Spell)
def create_spell(spell: schemas.SpellCreate, db: Session = Depends(get_db), key: str = ""):
    hashed = os.getenv("HASHED")
    if not bcrypt.checkpw(key, hashed):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    db_spell = utils.get_spell_by_name(db, spell_name=spell.name)
    if db_spell:
        raise HTTPException(
            status_code=400, detail="spell with that name allready created")
    return utils.create_spell(db=db, spell=spell)
