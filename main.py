import os
import git
import sys
from github import Github

def main():
    path = "C:\\Users\\T440p\\Desktop\\Projects"
    # Line was replaced by argument from the commandline
    #repoName = "repoName"
    repoName = str(sys.argv[1])
    newPath = path + "\\" + repoName
    userToken = "token"
    userName = "lepasq"
    remoteUrl = "https://github.com/" + userName + "/" + repoName + ".git"

    # Navigating to directory
    os.chdir(path)
    os.mkdir(repoName)
    os.chdir(repoName)
    os.system("touch README.md")

    # git init && git commit
    r = git.Repo.init(newPath)
    r.index.add("*")
    r.index.commit("initial commit")

    # Create repository on Github.com
    g = Github(userToken)
    user = g.get_user()
    repo = user.create_repo(repoName)

    # Adding remote to git repository & pushing to Github
    origin = r.create_remote('origin', remoteUrl)
    r.remotes.origin.push(refspec='master:master')

    # Open VSCode and open workspace
    os.system("code .")

main()