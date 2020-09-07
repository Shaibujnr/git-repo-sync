import git_repo_sync.config as config


def test_config():
    assert config.GIT_SOURCE_TOKEN
    assert config.GIT_SOURCE_USERNAME
    assert config.GIT_STATE_PATH == "/home/shaibu/Workspace/Python/data"