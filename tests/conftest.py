from typing import Any, Dict, List
from uuid import UUID
from pathlib import Path
from starlette.config import Config
import pytest
import json
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest_mock import MockFixture
from starlette.config import environ

environ["APP_ENV"] = "test"

import git_repo_sync.config as config
from git_repo_sync.app import app

example_folder: Path = Path(__file__).parents[1] / "examples"


@pytest.fixture
def push_payload() -> dict:
    push_payload_path = example_folder / "push.json"
    data = None
    with open(push_payload_path, "r") as fp:
        data = json.load(fp)
        assert "push" in data
    return data
