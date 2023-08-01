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
    
    DB_NAME = 'PG_Inisghts'  # This is used for the name of the backup file
                             # and must be set manually

    #  Variables below must be in a .env file located within same directory
    PASSWORD = os.getenv('SUPA_PASSWORD')
    SUPA_ID = os.getenv('SUPA_ID')
    DB_PORT = os.getenv('SUPA_PORT')
    USERNAME = os.getenv('SUPA_USER')
    #  URL below generated from the ID above and shouldn't be changed
    SUPA_URL = f'db.{SUPA_ID}.supabase.co'
    
    
settings = Settings()