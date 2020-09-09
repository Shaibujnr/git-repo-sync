from fastapi import FastAPI, Body, BackgroundTasks
from typing import Any
import git_repo_sync.util as util
from git_repo_sync.config import GIT_STATE_PATH

app = FastAPI()


def perform_sync(
    source_repository_url,
    source_repository_name,
    target_repository_url,
    target_username,
    target_token,
):
    if not util.does_repository_exist_locally(source_repository_name):
        print(
            f"\nRepository {source_repository_name} does not exist in path {GIT_STATE_PATH}..."
        )
        print("\n Cloning repository...")
        util.clone_repository(source_repository_url)

    assert util.does_repository_exist_locally(source_repository_name)

    print("\nUpdating local repository...")
    util.update_repository(source_repository_name)
    print("\n Update done")
    print("\n Syncing target repository..")
    util.sync_target(
        repo_name=source_repository_name,
        target_url=target_repository_url,
        target_username=target_username,
        target_token=target_token,
    )
    print("\nSync Done")


@app.post("/target")
def sync(
    url: str,
    username: str,
    token: str,
    background_tasks: BackgroundTasks,
    data: Any = Body(...),
):
    print("\nChecking data from webhook....")
    if any(item not in data for item in ["push", "repository"]):
        return
    print("\nData appears to be in the correct format....")
    repository = data["repository"]
    print("\nChecking if reposity is git or mercurial...")
    if repository["scm"] != "git":
        return
    print("\nConfirmed!! repository is git")
    source_repository_url = repository["links"]["html"]["href"] + ".git"
    print(f"\nSource repository url is {source_repository_url}")
    source_repository_name = repository["name"]
    print(f"\nSource repository name is {source_repository_name}")

    background_tasks.add_task(
        perform_sync,
        source_repository_url=source_repository_url,
        source_repository_name=source_repository_name,
        target_repository_url=url,
        target_username=username,
        target_token=token,
    )
    return
