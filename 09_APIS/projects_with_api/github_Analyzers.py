
# GitHub Repository Analyzer
# API endpoints
# Headers (professional API usage)
# Parsing large JSON responses
# Handling missing data
# Finding the most starred repository
# Structuring code cleanly
import requests


def get_user_data(username):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    return response.json()


def get_repositories(username):

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    return response.json()


def find_top_repo(repos):

    top_repo = None
    max_stars = -1

    for repo in repos:

        stars = repo["stargazers_count"]

        if stars > max_stars:
            max_stars = stars
            top_repo = repo["name"]

    return top_repo, max_stars


username = input("Enter GitHub username: ")

user = get_user_data(username)

repos = get_repositories(username)

top_repo, stars = find_top_repo(repos)

print("\nGitHub Profile Report")
print("---------------------")

print("User:", user["login"])
print("Followers:", user["followers"])
print("Public Repos:", user["public_repos"])
print("Top Repo:", top_repo)
print("Stars:", stars)