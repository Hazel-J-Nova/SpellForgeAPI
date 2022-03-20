from sqlalchemy.orm import Session
import models

import schemas


def get_spell(db: Session, spell_id: int):
    return db.query(models.Spells).filter(models.Spell.id == spell_id).first()


def get_spells(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Spells).offset(skip).limit(limit).all()


def get_spell_by_name(db: Session, spell_name: str):
    return db.query(models.Spells).filter(models.Spells.name == spell_name).first()


def create_spell(db: Session, spell: schemas.SpellCreate):
    db_spell = models.Spells(**spell.dict())
    db.add(db_spell)
    db.commit()
    db.refresh(db_spell)
    return db_spell


def create_spell_classes(db: Session, character_class: schemas.CharacterClassCreate, spell_id: int):
    db_character_class = models.Character_Class(
        **character_class.dict(), spell_id=spell_id)
    db.add(db_character_class)
    db.commit()
    db.refresh(db_character_class)
    return db_character_class


def create_spell_component(db: Session, spell_component: schemas.SpellComponentCreate, spell_id: int):
    db_spell_component = models.Spell_Component(
        **spell_component.dict(), spell_id=spell_id)
    db.add(db_spell_component)
    db.commit()
    db.refresh(db_spell_component)
    return db_spell_component
