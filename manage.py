import os
import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from db.db import db


MIGRATION_DIR = os.path.join('db', 'migrations')
Migrate = Migrate(app, db, directory=MIGRATION_DIR)

Manager = Manager(app)
# Define the migration command to always be preceded by the word "db"
Manager.add_command('db', MigrateCommand)


# define our command for testing called "test"
# Usage: python manage.py test
@Manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('./specs', pattern='*_spec.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    Manager.run()
