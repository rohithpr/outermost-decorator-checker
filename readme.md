# Outermost Decorator Checker

Github Action to ensure that a specified decorator is the outermost decorator for any function.

Currently, only Python 2.7 is supported since the primary target of this Github Action is a legacy repo using Python 2.7.

# Using this Github Action

Add the following workflow to your repository to use this Github Action:

```yml
on: [pull_request]

jobs:
  outermost_decorator_checker:
    runs-on: ubuntu-latest
    name: Outermost Decorator Checker
    steps:
      - uses: actions/checkout@v2 # outermost_decorator_checker needs a copy of your repo to find any issues.
        with:
          fetch-depth: 0
      - name: Step Name
        id: step_id
        uses: rohithpr/outermost-decorator-checker@master
        env:
          DECORATOR_NAME: DECORATOR_NAME # Name of the decorator that should be the outermost decorator if it is used.
          SPECIFIED_DIR: DIR_NAME # Optional environment variable if the checker should only look at files in a specified directory.
```

# How it works

`service.py` enumerates all the Python files in the repo and passes them off to
`checker.py`. Here, Python's inbuilt `ast` module is used to get the Abstract
Syntax Tree of each file. The action then goes through your code's AST to
identify any functions that are using the decorator mentioned above, but don't
have it as the outermost decorator.

If there are any issues, a message is printed to the console with details of
offending methods and an exception is raised. At this point of time, a message
is not posted on the PR itself, but only the status check fails.

#### A successful status check:
<img width="736" alt="Status Check Success" src="https://user-images.githubusercontent.com/10276811/89878602-5ea0ae00-dbdf-11ea-8ad0-ad7afcd2bd01.png">

#### A failed status check:
<img width="715" alt="Status Check Fail" src="https://user-images.githubusercontent.com/10276811/89878633-695b4300-dbdf-11ea-94bc-d711878a87b3.png">
