# -*- coding: utf-8 -*-


import sys
from pathlib import Path

if str(Path(__file__).parent) not in sys.path:
    sys.path.append(str(Path(__file__).parent))

from helpers.session import DbConnect


class SupaDbBackup(DbConnect):

    db_obj = None
    
    def __init__(self):
        super().__init__()
    
#    @classmethod
#    def _set_db_on
    
    
if __name__ == "__main__":
    print(DbConnect.get_db)