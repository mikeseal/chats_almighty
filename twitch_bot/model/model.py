from typing import List
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, ForeignKeyConstraint, Index, Integer, String
from models import Base, Channels, Commands, Links

engine = create_engine('mysql://root:nlhpOquNrGXfotANzQNQrbwGIVdBqvUd@192.168.120.249:3306')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)