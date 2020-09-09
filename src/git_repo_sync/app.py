from fastapi import FastAPI, Body, BackgroundTasks
from typing import Any
import git_repo_sync.util as util

app = FastAPI()


def perform_sync(
    source_repository_url,
    source_repository_name,
    target_repository_url,
    target_username,
    target_token,
):
    if not util.does_repository_exist_locally(source_repository_name):
        util.clone_repository(source_repository_url)

    assert util.does_repository_exist_locally(source_repository_name)

    util.update_repository(source_repository_name)
    util.sync_target(
        repo_name=source_repository_name,
        target_url=target_repository_url,
        target_username=target_username,
        target_token=target_token,
    )


@app.post("/target")
def sync(
    url: str,
    username: str,
    token: str,
    background_tasks: BackgroundTasks,
    data: Any = Body(...),
):
    if any(item not in data for item in ["push", "repository"]):
        return
    repository = data["repository"]
    if repository["scm"] != "git":
        return

    source_repository_url = repository["links"]["html"]["href"] + ".git"
    source_repository_name = repository["name"]

    background_tasks.add_task(
        perform_sync,
        source_repository_url=source_repository_url,
        source_repository_name=source_repository_name,
        target_repository_url=url,
        target_username=username,
        target_token=token,
    )
    return
