from playwright.sync_api import APIRequestContext, Page

from pages.github_page import GitHubPage
from tests.conftest import GITHUB_USER, GITHUB_REPO, password, bug_name, bug_desc, set_up_teardown


def test_last_created_issue_should_be_first_in_the_list(api_request_context: APIRequestContext, set_up_teardown: Page) -> None:
    page = set_up_teardown
    github = GitHubPage(page)
    github.create_issue(api_request_context, "[Feature] request 1", "Feature description")
    github.create_issue(api_request_context, "[Feature] request 2", "Feature description")
    page.goto(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues")
    github.check_first_issue("[Feature] request 2")


def test_last_created_issue_should_be_on_the_server(api_request_context: APIRequestContext, set_up_teardown: Page) -> None:
    page = set_up_teardown
    github = GitHubPage(page)
    github.login_to_github_website(GITHUB_USER, password)
    github.create_and_check_issue(bug_name, bug_desc, api_request_context)

