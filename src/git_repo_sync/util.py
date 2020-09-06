import os
from git import Repo
from pathlib import Path
from git_repo_sync.config import GIT_STATE_PATH

repo_folder_path: Path = Path(GIT_STATE_PATH)


def does_repository_exist_locally(repository_name):
    repo = repo_folder_path / repository_name
    if not os.path.exists(repo):
        return False
    git_folder = repo / ".git"
    return bool(os.path.exists(git_folder))
