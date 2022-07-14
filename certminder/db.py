#!/usr/bin/env python3

import os

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

from certminder import config


engine = create_engine('sqlite:///' + os.path.expanduser(config.db_file))
session = sessionmaker(bind=engine)

Base = declarative_base()


class Result(Base):
    __tablename__ = 'results'
    __table_args__ = (
        UniqueConstraint('host', 'port'),
    )

    id = Column(Integer, primary_key=True)
    host = Column(String)
    port = Column(String)
    start = Column(Boolean)
    end = Column(Boolean)
    name = Column(Boolean)
    valid = Column(Boolean)
    updated = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, host, port, start, end, name, valid):
        self.host = host
        self.port = port
        self.start = start
        self.end = end
        self.name = name
        self.valid = valid

    @classmethod
    def create_or_update(cls, session, host, port,
                         start, end, name, valid):
        instance = session.query(cls).filter_by(host=host,
                                                port=port).one_or_none()

        if instance:
            instance.start = start
            instance.end = end
            instance.name = name
            instance.valid = valid
        else:
            instance = cls(host, port, start, end, name, valid)
            session.add(instance)

        session.commit()
        return instance


Base.metadata.create_all(engine)
