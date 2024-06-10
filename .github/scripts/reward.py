import os

import dotenv
import requests


def reward_contributor(
    gh_token: str,
    repo_full_name: str, 
    pr_number: int
) -> bool:
    url = f"https://one.lightningbounties.com/api/rewards/check/pull-request"
    body = {
        "github_token": gh_token,
        "repo_full_name": repo_full_name,
        "pull_request_number": pr_number
    }

    response = requests.post(url, json=body)
    print(response.json())

    return True


def main() -> None:
    dotenv.load_dotenv()

    github_token = os.getenv("GITHUB_TOKEN")
    repo_full_name = os.getenv("REPO_FULL_NAME")
    pull_request_number = int(os.getenv("PULL_REQUEST_NUMBER"))

    try:
        reward_result = reward_contributor(github_token, repo_full_name, pull_request_number)
    except RuntimeError:
        print('Could not check rewards. Please contact support.')


if __name__ == '__main__':
    main()
