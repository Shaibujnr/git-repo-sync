import git_repo_sync.util as util
from git_repo_sync.config import GIT_STATE_PATH


def test_git_repo_exists():
    assert util.does_repository_exist_locally("test_git_repo")


def test_folder_exists_but_not_as_repo():
    import os

    folder_path = f"{GIT_STATE_PATH}/test_folder"
    assert os.path.exists(folder_path)
    assert os.path.isdir(folder_path)
    assert not util.does_repository_exist_locally("test_folder")


def test_clone_repository():
    test_url = "https://bitbucket.org/shaibujnr/git_repos_sync.git"
    assert not util.does_repository_exist_locally("git_repos_sync")
    repo = util.clone_repository(test_url)
    assert util.does_repository_exist_locally("git_repos_sync")


def test_update_repository():
    repo_name = "git_repos_sync"
    util.update_repository(repo_name)
