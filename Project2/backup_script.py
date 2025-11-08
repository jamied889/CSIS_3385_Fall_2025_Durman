# backup_script.py
# Deprecated backup system (do not use)

import os
import shutil

def backup_database():
    source = './seed.json'
    destination = './backup/'
    if not os.path.exists(destination):
        os.makedirs(destination)
    shutil.copy(source, os.path.join(destination, 'seed_backup.json'))

# TODO: Integrate into nightly CRON job
