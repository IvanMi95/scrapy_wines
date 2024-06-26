from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from project.database import Base


class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, autoincrement=True)
    wine_id = Column(Integer, ForeignKey('wine.id'), nullable=False)
    # TODO Maybe remove foreign key
    source = Column(String(128), nullable=False)
    score = Column(Float,  nullable=True)
    reviews = Column(Integer,  nullable=True)
# TODO add created at colum

    wine = relationship("Wine", back_populates="rating")
