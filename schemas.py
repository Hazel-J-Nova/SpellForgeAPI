from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

from pydantic.types import conint


class SpellComponentBase(BaseModel):
    spell_component_name = str


class SpellComponentCreate(SpellComponentBase):
    pass


class SpellComponent(SpellComponentBase):
    id: int
    spell_id: int

    class Config:
        orm_mode = True


class CharacterClassBase(BaseModel):
    character_class_name = str


class CharacterClassCreate(CharacterClassBase):
    pass


class CharacterClass(CharacterClassBase):
    id: int
    spell_id: int

    class Config:
        orm_mode = True


class SpellBase(BaseModel):
    name: str
    Character_Class: str
    spell_level: str

    spell_source: str
    spell_school: str
    description: str
    casting_time: str
    duration: str
    range_or_area: str

    Spell_Component: str
    spell_save_or_attack: str
    spell_damage_type: str


class SpellCreate(SpellBase):
    pass


class Spell(SpellBase):
    id: int
    spell_character_classes: list[CharacterClass] = []
    spell_components: list[SpellComponent] = []

    class Config:
        orm_mode = True
