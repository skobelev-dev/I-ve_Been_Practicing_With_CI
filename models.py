from sqlalchemy import Column, String, Integer, Time

from database import Base, sync_engine

class Recipe(Base):
    __tablename__ = 'Recipe'
    id = Column(Integer, primary_key=True, index=True)
    tittle = Column(String, index=True)
    views = Column(Integer, index=True, default=0) # Количество просмотров
    cooking_time = Column(Time, index=True)
    description = Column(String, index=True)
    ingredient_list = Column(String, index=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.metadata.create_all(sync_engine)