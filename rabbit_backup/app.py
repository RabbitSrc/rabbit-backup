import sys

from rabbit_dropbox import BackupJob

access_token = 'Z5h-tGQBxE4AAAAAAAABKgATEpeCx5rp7Gw8mqZ76dCDBXhCHkFnrWJFLCgOfwia'
# backup_remote_folder = 'backup_folder'
retention_days = 1
file = "/Users/guoliang/Downloads/ibm.pdf"


def main(argv):
    print argv
    backup_remote_folder = argv[1]
    file_list = argv[2:]
    backup_job = BackupJob(access_token, backup_remote_folder, retention_days)
    for f in file_list:
        backup_job.backup_and_clear_history_data(f)

if __name__ == "__main__":
    main(sys.argv)