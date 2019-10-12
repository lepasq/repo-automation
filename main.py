import os
import git
from github import Github

path = "C:\\Users\\T440p\\Desktop\\Projects"
newDir = "cmdline_will_be_added"
newPath = path + "\\" + newDir
repoName = "taskAutomation"
userToken = "insert_your_token_here"


# Navigating to directory
os.chdir(path)
os.mkdir(newDir)
os.chdir(newDir)
os.system("touch README.md")


# git init && git commit
r = git.Repo.init(newPath)
r.index.add("*")
r.index.commit("initial commit")


# Create repository on Github.com
g = Github(userToken)
user = g.get_user()
repo = user.create_repo(repoName)