import pytest
from pprint import pprint


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")

    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")

    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")

    assert r["total_count"] == 58


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")

    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("A")

    assert r["total_count"] != 0


@pytest.mark.api
def test_get_all_emojis(github_api):
    r = github_api.get_all_emojis()

    assert r["code"] == 200
    assert len(r["body"]) > 0


@pytest.mark.api
def test_get_specified_emoji(github_api):
    r = github_api.get_all_emojis()
    emoji_to_check = "1st_place_medal"

    assert emoji_to_check in r["body"].keys()


@pytest.mark.api
def test_get_commits_for_exist_repo(github_api, test_user):
    owner = test_user.owner
    repo = test_user.repo

    r = github_api.get_all_commits(owner, repo)

    assert len(r) > 0


@pytest.mark.api
def test_get_commits_for_not_exist_repo(github_api, test_user):
    owner = test_user.owner
    repo = "not_exist"
    documentation_url_to_check = (
        "https://docs.github.com/rest/commits/commits#list-commits"
    )

    r = github_api.get_all_commits(owner, repo)

    assert r["message"] == "Not Found"
    assert r["documentation_url"] == documentation_url_to_check


@pytest.mark.api
def test_get_specified_commit(github_api, test_user):
    sha_commit = "60d9e519b37bb62128222811ce1b70ba55861406"
    owner = test_user.owner
    repo = test_user.repo

    r = github_api.get_commit(owner, repo, sha_commit)

    assert r["code"] == 200
    assert "feat: Project task 3" in r["body"]["commit"]["message"]
