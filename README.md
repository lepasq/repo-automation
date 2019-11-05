# Repository Automation

Python program, that speeds up the process of setting up projects.

## Install

```git
git clone https://github.com/lepasq/repo-automation.git
```

## Setup

In order to get the program running, a few variables need to be changed.

![alt Screenshot](https://github.com/lepasq/repo-automation/blob/master/screenshots/python.png "Variables to be changed inside main.py")  

Inside ``main.py``, **path**, **userToken** and **userName** have to be changed.  
Correct formatting for Windows:  
``C:\\Users\\T440p\\Desktop\\Projects``

![alt Screenshot](https://github.com/lepasq/repo-automation/blob/master/screenshots/batch.png "Path to be changed inside create.bat")

Inside create.bat, the **directory**, in which the automation repository is located has to be changed
Correct formatting for Windows: ``C:\Users\T440p\Desktop\Projects\Repository-Automation``

## Add to Windows Command Prompt

In order to use the program inside your command prompt, the folder containing the repository has to be added to the **environment variables.**

In order to open the environment variables, type **env** in the windows search bar and hit enter
Click on **"Environment Variables"**.

Edit the user variable **"Path"** (or create a new user variable with the variable name Path, it if it doesn't exist yet).
Enter the location of the directory containing this repository in the variable name.

Your window should now look like this:

![alt Screenshot](https://github.com/lepasq/repo-automation/blob/master/screenshots/env.png "Environment Variables window")

In order to execute the command, you need to type

```bash
create name
```

 where _name_ is your desired name of the repository that shall be created.
