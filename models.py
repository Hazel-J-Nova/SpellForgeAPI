from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Spells(Base):
    __tablename__ = "spell"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    Character_Class = Column(String, nullable=False)
    spell_level = Column(String, nullable=True)
    spell_source = Column(String, nullable=True)
    spell_school = Column(String, nullable=True)
    casting_time = Column(String, nullable=False)
    duration = Column(String, nullable=False)
    range_or_area = Column(String, nullable=False)
    Spell_Component = Column(String, nullable=True)
    description = Column(String, nullable=False)
    spell_save_or_attack = Column(String, nullable=False)
    spell_damage_type = Column(String, nullable=False)
