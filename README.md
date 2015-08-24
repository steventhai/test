# repos.py
Make GET request to retrieve information to Github search api.

Usage:

python repos.py keyword limit

keyword: a string to search for, e.g: "search something"
limit: limit number of returned repositories (1 <= limit <= 100).

Note: I used requests package, so if your machine doesn't have it, you need to install requests package.
