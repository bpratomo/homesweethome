WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Teknikfisika123@localhost:5432/homesweethome_flask'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')