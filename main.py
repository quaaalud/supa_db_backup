# -*- coding: utf-8 -*-


import sys
from pathlib import Path

if str(Path(__file__).parent) not in sys.path:
    sys.path.append(str(Path(__file__).parent))

from helpers.session import DbConnect


class SupaDbBackup:
    db_obj = ...