from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

GITHUB_API_TOKEN = input("input your github token: ")
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set"

GITHUB_USER = input("input your github username: ")
assert GITHUB_USER, "GITHUB_USER is not set"

GITHUB_REPO = "test_API"

password = input("input your github password: ")

i_name = "[Feature] request 2"
bug_name = "Bug report 1"
bug_desc = "Bug description"


@pytest.fixture()
def set_up_teardown(page) -> None:
    # browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    # context = browser.new_context()
    # page = context.new_page()
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues")
    yield page
    # context.close()
    # browser.close()


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        # We set this header per GitHub guidelines.
        "Accept": "application/vnd.github.v3+json",
        # Add authorization token to all requests.
        # Assuming personal access token available in the environment.
        "Authorization": f"token {GITHUB_API_TOKEN}",
    }
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session", autouse=True)
def create_test_repository(
    api_request_context: APIRequestContext,
) -> Generator[None, None, None]:
    # Before all
    new_repo = api_request_context.post("/user/repos", data={"name": GITHUB_REPO})
    assert new_repo.ok
    yield
    # After all
    deleted_repo = api_request_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_REPO}")
    assert deleted_repo.ok
