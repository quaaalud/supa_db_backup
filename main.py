# -*- coding: utf-8 -*-


import sys
from pathlib import Path

if str(Path(__file__).parent) not in sys.path:
    sys.path.append(str(Path(__file__).parent))

from helpers.session import DbConnect


class SupaDbBackup(DbConnect):
    
    def __init__(self):
        super().__init__()
        self.pg_dump_command = f'pg_dump "{self.DB_URL}" > "{self.SAVE_PATH}"'
    
    
if __name__ == "__main__":
    import subprocess
    
    supa_db_obj = SupaDbBackup()
    print('Starting DB Copy')
    subprocess.run(supa_db_obj.pg_dump_command, shell=True, check=True)
    print('The DB has been copied and saved as {supa_db_obj.SAVE_NAME}')