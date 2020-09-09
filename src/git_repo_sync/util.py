import os
from git import Repo, Remote
from git.cmd import Git
from git.exc import GitCommandError
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


def authenicated_url(username, token, git_url):
    protocol, url = git_url.split("//")
    return f"{protocol}//{username}:{token}@{url}"


def clone_repository(git_url: str) -> Repo:
    repo_url = git_url
    if "@" not in repo_url:
        # no authentication details
        repo_url = authenicated_url(GIT_SOURCE_USERNAME, GIT_SOURCE_TOKEN, repo_url)
    repo_name = repo_url.split("/")[-1].split(".")[0]
    target_path = repo_folder_path / repo_name
    return Repo.clone_from(url=repo_url, to_path=target_path)


def update_repository(repo_name: str) -> Repo:
    repo_path = repo_folder_path / repo_name

    repo = Repo(repo_path)
    git = Git(working_dir=repo_path)
    # git.fetch(all=True)

    current_branch = repo.active_branch
    origin = repo.remotes.origin
    origin.update()

    for ref in origin.refs:
        branch_name = str(ref).split("/")[-1]
        git.checkout(branch_name)
        git.pull(all=True)

    git.checkout(current_branch)


def sync_target(repo_name, target_url, target_username, target_token):
    repo_path = repo_folder_path / repo_name
    repo = Repo(repo_path)
    git = Git(working_dir=repo_path)
    if "target" in repo.remotes:
        Remote.remove(repo, "target")
        # repo.remotes.target.rm()

    authenticated_target_url = authenicated_url(
        target_username, target_token, target_url
    )
    repo.create_remote("target", authenticated_target_url)
    try:
        git.push(["target", "*:*"])
        git.push("target", all=True)
    except GitCommandError as e:
        checks = ["remote rejected", "deny updating a hidden ref"]
        if any(check not in str(e) for check in checks):
            raise e