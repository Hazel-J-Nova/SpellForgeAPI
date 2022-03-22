import re
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


models.Base.metadata.create_all(bind=engine)


@app.get("/spells/", response_model=list[schemas.Spell],
         )
def read_spells(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    spells = utils.get_spells(db, skip=skip, limit=limit)
    return spells


@app.get("/spells/{spell_name}", response_model=schemas.Spell)
def get_spell(spell_name: str, db: Session = Depends(get_db),):
    spell = utils.get_spell_by_name(db, spell_name)
    return spell


app.post("/test")


def run_test(request: Request):
    return "ya girl"


@app.post("/spells/")
def create_spell(request: Request, spell: schemas.SpellCreate, db: Session = Depends(get_db), ):
    key = request.query_params["key"]
    salt = bcrypt.gensalt(4)
    key = key.encode('utf-8')
    hashed = bcrypt.hashpw(key, salt)
    hashedKey = bcrypt.hashpw(key, salt)
    if not hashed == hashedKey:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    db_spell = utils.get_spell_by_name(db, spell_name=spell.name)
    print(db_spell)
    if db_spell:
        raise HTTPException(
            status_code=400, detail="spell with that name allready created")
    return utils.create_spell(db=db, spell=spell)
