#!/usr/bin/env python3

import os
import git
import sys
from github import Github

user_token = "token"
user_name = "username"
repo_name = str(sys.argv[1])
code_editor = "vim"
remote_url = "https://github.com/" + user_name + "/" + repo_name + ".git"

# Navigating to directory
os.mkdir(repo_name)
os.chdir(repo_name)
os.system("touch README.md")

# git init && git commit
r = git.Repo.init(".")
r.index.add("*")
r.index.commit("Initial commit")

# Create repository on Github.com
g = Github(user_token)
user = g.get_user()
repo = user.create_repo(repo_name)

# Adding remote to git repository & pushing to Github
origin = r.create_remote('origin', remote_url)
r.remotes.origin.push(refspec='master:master')

# Open directory code editor
os.system(code_editor + " .")
os.system("echo Successful build!")
