from git_repo_sync.util import does_repository_exist_locally
from git_repo_sync.config import GIT_STATE_PATH


def test_git_repo_exists():
    assert does_repository_exist_locally("test_git_repo")


def test_folder_exists_but_not_as_repo():
    import os

    folder_path = f"{GIT_STATE_PATH}/test_folder"
    assert os.path.exists(folder_path)
    assert os.path.isdir(folder_path)
    assert not does_repository_exist_locally("test_folder")
