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


def test_authenticated_url():
    username = "testusername"
    token = "testtoken"
    url = "https://gitremote.com/username/repo.git"
    expected_result = "https://testusername:testtoken@gitremote.com/username/repo.git"
    result = util.authenicated_url(username, token, url)
    assert expected_result == result


def test_clone_repository():
    test_url = "https://bitbucket.org/shaibujnr/git_repos_sync.git"
    assert not util.does_repository_exist_locally("git_repos_sync")
    util.clone_repository(test_url)
    assert util.does_repository_exist_locally("git_repos_sync")


def test_update_repository():
    repo_name = "git_repos_sync"
    util.update_repository(repo_name)


def test_sync_repository():
    repo_name = "git_repos_sync"
    util.sync_target(
        repo_name,
        "https://gitlab.com/shaibujnr/git_repos_sync.git",
        "shaibujnr",
        "Vwyrz_4az8FojXAWNH2x",
    )
