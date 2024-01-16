from playwright.sync_api import APIRequestContext

from pages.github_page import GitHubPage


def test_should_create_bug_report(api_request_context: APIRequestContext, page) -> None:
    github = GitHubPage(page)
    github.create_issue(api_request_context, "[Bug] report 1", "Bug description")
    issues_response = github.get_issues(api_request_context)
    github.check_issue_api(issues_response, "[Bug] report 1", "Bug description")


def test_should_create_feature_request(api_request_context: APIRequestContext, page) -> None:
    github = GitHubPage(page)
    github.create_issue(api_request_context, "[Feature] request 1", "Feature description")
    issues_response = github.get_issues(api_request_context)
    github.check_issue_api(issues_response, "[Feature] request 1", "Feature description")

