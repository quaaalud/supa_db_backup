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
    DB_URL = settings.SUPA_BACKUP_URL
    
    _dirpath = Path(__file__).parents[1]
    
    SAVE_DIR = Path(_dirpath, 'backups') 
    SAVE_PATH = Path(SAVE_DIR, f'{DB_NAME} {datetime.now()}.sql')
    
    def __init__(self):
        self.SAVE_DIR.mkdir(parents=False, exist_ok=True)
        pass
