import json
from datetime import time
from typing import List
from pydantic import BaseModel, field_validator


class Recipe(BaseModel):
    tittle: str
    cooking_time: time
    ingredient_list: List[str]
    description: str

    @field_validator('ingredient_list', mode='before')
    @classmethod
    def parse_ingredient_list(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return [v]
        return v

    class Config:
        from_attributes=True