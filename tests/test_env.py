# This unit test ensures that the identidoc environment is correctly set up.
# If this unit test fails, the current version of identiDoc should not be deployed.

import unittest
import os

class TestEnv(unittest.TestCase):
    # Add to this unit test as environment variables are created/modified
    def test_env_vars(self):
        upload_path = os.environ.get('IDENTIDOC_UPLOAD_PATH', 'ERROR')
        temp_path = os.environ.get('IDENTIDOC_TEMP_PATH', 'ERROR')
        db_path = os.environ.get('IDENTIDOC_DB', 'ERROR')

        assert upload_path is not 'ERROR'
        assert temp_path is not 'ERROR'
        assert db_path is not 'ERROR'