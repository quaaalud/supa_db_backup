#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:42:42 2023

@author: dale
"""

from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers.config import settings


class DbConnect:

    DB_ENGINE = create_engine(settings.DB_URL)

    SESSION = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=DB_ENGINE
    )
    
    def __init__(self):
        pass

    @classmethod
    def get_db(cls) -> Generator:
        try:
            db = cls.SESSION()
            yield db
        finally:
            db.close()
