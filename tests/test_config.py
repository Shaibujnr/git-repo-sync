import git_repo_sync.config as config


def test_config():
    assert config.GIT_SOURCE_TOKEN == "testtoken"
    assert config.GIT_SOURCE_USERNAME == "testusername"
    assert config.GIT_STATE_PATH == "/home/shaibu/Workspace/Python/data"