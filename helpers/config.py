#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:31:59 2023

@author: dale
"""


import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    
    SUPA_PASSWORD = os.getenv('SUPA_PASSWORD')
    SUPA_ID = os.getenv('SUPA_ID')
    SUPA_PORT = os.getenv('SUPA_PORT')
    SUPA_URL = f'{SUPA_PASSWORD}@db.{SUPA_ID}.supabase.co:{SUPA_PORT}'
    DB_URL: str = f'postgresql://postgres:{SUPA_URL}/postgres'
    
    
settings = Settings()