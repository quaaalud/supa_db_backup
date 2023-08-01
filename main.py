# -*- coding: utf-8 -*-


import sys
import subprocess
from pathlib import Path

if str(Path(__file__).parent) not in sys.path:
    sys.path.append(str(Path(__file__).parent))

from helpers.session import DbConnect


class SupaDbBackup(DbConnect):
    
    def __init__(self):
        super().__init__()
        db_copy_command = ' '.join(
            [
              self.connect_str, 
              '-f', 
              self.save_path
            ]
        )
        try:
            subprocess.run(db_copy_command, shell=True, check=True)
        except Exception as e:
            print(f"An error occurred while backing up the database: {e}")
        
    
    
if __name__ == "__main__":
    backup_obj = SupaDbBackup()

    