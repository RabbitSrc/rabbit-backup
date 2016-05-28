import os
import unittest
from rabbit_backup.rabbit_dropbox import BackupJob

current_path = os.path.dirname(os.path.realpath(__file__))


def get_access_token_for_t():
    dropbox_key = "DROPBOX_ACCESS_TOKEN_FOR_TESTING"
    try:
        return os.environ[dropbox_key]
    except KeyError:
        raise RuntimeError('No dropbox testing key found, please set the Enviroment variable: "%s"' % dropbox_key)


class TestPyBackup(unittest.TestCase):

    def setUp(self):
        access_token_for_testing = get_access_token_for_t()
        self.backup_job = BackupJob(access_token_for_testing, 'backup_test', 1)
        self.test_file_full_path = os.path.join(current_path, 'test-file_for_uploading')
        f = open(self.test_file_full_path, 'w')
        f.write('test-data')
        f.close()

    def test_login(self):
        self.assertTrue('@' in self.backup_job.account['email'])

    def test_upload(self):
        self.backup_job.backup_and_clear_history_data([self.test_file_full_path])

    @unittest.skip('skip the download testing')
    def test_download(self):
        self.backup_job.rabbit_dropbox.get_file("/tmp/test-file", "ibm.pdf")

    def tearDown(self):
        if os.path.isfile(self.test_file_full_path):
            os.remove(self.test_file_full_path)

if __name__ == '__main__':
    unittest.main()
