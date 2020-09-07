import os
from git import Repo
from pathlib import Path
from git_repo_sync.config import (
    GIT_STATE_PATH,
    GIT_SOURCE_USERNAME,
    GIT_SOURCE_TOKEN,
)

repo_folder_path: Path = Path(GIT_STATE_PATH)


def does_repository_exist_locally(repository_name):
    # Todo more checks?
    repo = repo_folder_path / repository_name
    if not os.path.exists(repo):
        return False
    git_folder = repo / ".git"
    return bool(os.path.exists(git_folder))


def clone_repository(git_url: str) -> Repo:
    repo_url = git_url
    if "@" not in repo_url:
        # no authentication details
        protocol, url = git_url.split("//")
        repo_url = f"{protocol}//{GIT_SOURCE_USERNAME}:{GIT_SOURCE_TOKEN}@{url}"
    repo_name = repo_url.split("/")[-1].split(".")[0]
    target_path = repo_folder_path / repo_name
    return Repo.clone_from(url=repo_url, to_path=target_path)
