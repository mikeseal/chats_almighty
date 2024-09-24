from typing import List

from sqlalchemy import ForeignKeyConstraint, Index, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Channels(Base):
    __tablename__ = 'channels'
    __table_args__ = (
        Index('channel_name', 'channel_name', unique=True),
        Index('idx_channels_name', 'channel_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_name: Mapped[str] = mapped_column(String(255))

    commands: Mapped[List['Commands']] = relationship('Commands', back_populates='channel')


class Commands(Base):
    __tablename__ = 'commands'
    __table_args__ = (
        ForeignKeyConstraint(['channel_id'], ['channels.id'], name='commands_ibfk_1'),
        Index('channel_id', 'channel_id', 'command_name', unique=True),
        Index('idx_commands_name_channel_id', 'command_name', 'channel_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(Integer)
    command_name: Mapped[str] = mapped_column(String(255))

    channel: Mapped['Channels'] = relationship('Channels', back_populates='commands')
    links: Mapped[List['Links']] = relationship('Links', back_populates='command')


class Links(Base):
    __tablename__ = 'links'
    __table_args__ = (
        ForeignKeyConstraint(['command_id'], ['commands.id'], name='links_ibfk_1'),
        Index('command_id', 'command_id', unique=True),
        Index('idx_links_command_id', 'command_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    command_id: Mapped[int] = mapped_column(Integer)
    linktext: Mapped[str] = mapped_column(String(255))

    command: Mapped['Commands'] = relationship('Commands', back_populates='links')



engine = create_engine('sqlite:///users.db')
   Base.metadata.create_all(engine)
   Session = sessionmaker(bind=engine)