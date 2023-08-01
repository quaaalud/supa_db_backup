#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:42:42 2023

@author: dale
"""

from pathlib import Path
from datetime import datetime
from helpers.config import settings

class DbConnect:

    DB_NAME = settings.DB_NAME
    DB_URL = settings.SUPA_URL
    DB_USER = settings.USERNAME
    DB_PASSWORD = settings.PASSWORD
    DB_PORT = settings.DB_PORT
    
    _DATE_STR = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    _FILE_DIR = Path(__file__).parent
    SAVE_DIR = Path(_FILE_DIR, 'backups') 
    
    
    COMMAND_LIST = [
        'pg_dump', 
        f'-h {DB_URL}',
        f'-p {DB_PORT}',
        f'-d {DB_PASSWORD}',
        f'-U {DB_USER}'
    ]
    
    def __init__(self):
        self.SAVE_DIR.mkdir(parents=False, exist_ok=True)
        self.save_path = str(
            Path(
                self.SAVE_DIR,
                f'{self.DB_NAME}-{self._DATE_STR}.sql'
            )
        )
        self.connect_str = ' '.join(self.COMMAND_LIST)
        
