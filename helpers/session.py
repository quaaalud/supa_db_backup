#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:42:42 2023

@author: dale
"""

from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


class DbConnect:

    db_engine = create_engine(settings.SUPA_URL)

    SupaLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=db_engine
    )

    @classmethod
    def get_supa_db(cls) -> Generator:
        try:
            db = cls.SupaLocal()
            yield db
        finally:
            db.close()
