from playwright.sync_api import Page, expect, APIRequestContext

from tests.conftest import GITHUB_USER, GITHUB_REPO


class GitHubPage:
    def __init__(self, page: Page):
        self.page = page
        self._first_issue = page.locator("a[data-hovercard-type='issue']").first
        self._new_issue_locator = page.locator("text=New issue")
        self._sign_up_for_github_locator = page.get_by_label("Sign up for GitHub").get_by_role("link", name="Sign in")
        self._username_locator = page.get_by_label("Username or email address")
        self._password_locator = page.get_by_label("Password")
        self._sign_in_button_locator = page.get_by_role("button", name="Sign in", exact=True)
        self._title_locator = page.get_by_placeholder("Title")
        self._description_locator = page.locator("#issue_body")
        self._submit_new_issue_button_locator = page.get_by_role("button", name="Submit new issue")

    def create_issue(self, api_request_context: APIRequestContext, title: str, description: str):
        data = {
            "title": title,
            "body": description,
        }
        new_issue = api_request_context.post(
            f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
        )
        assert new_issue.ok

    def check_first_issue(self, i_name: str):
        first_issue = self._first_issue
        expect(first_issue).to_have_text(i_name)

    def login_to_github_website(self, GITHUB_USER, password):
        self._new_issue_locator.click()
        self._sign_up_for_github_locator.click()
        self._username_locator.click()
        self._username_locator.fill(GITHUB_USER)
        self._password_locator.click()
        self._password_locator.fill(password)
        self._sign_in_button_locator.click()

    def create_and_check_issue(self, bug_name, bug_desc, api_request_context: APIRequestContext):
        self._title_locator.fill(bug_name)
        self._description_locator.fill(bug_desc)
        self._submit_new_issue_button_locator.click()
        issue_id = self.page.url.split("/")[-1]
        new_issue = api_request_context.get(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues/{issue_id}")
        assert new_issue.ok

    def create_issue_api(self, api_request_context: APIRequestContext, title: str, description: str):
        data = {
            "title": title,
            "body": description,
        }
        new_issue = api_request_context.post(
            f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
        )
        assert new_issue.ok

    def get_issues(self, api_request_context: APIRequestContext):
        issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
        assert issues.ok
        return issues.json()

    def check_issue_api(self, issues_response: list, title: str, description: str):
        issue = list(
            filter(lambda issue: issue["title"] == title, issues_response)
        )[0]
        assert issue
        assert issue["body"] == description
