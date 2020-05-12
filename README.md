# Repository Automation

This repository contains a python script, that speeds up the process of setting up projects.

Running the script will initialize a local repository, add an empty README.md and push it to Github.

## Install

```git
git clone https://github.com/lepasq/repo-automation.git
```

## Setup

In order to get the program running, a few variables need to be changed.

![alt Screenshot](https://github.com/lepasq/repo-automation/blob/master/screenshots/python.png "Variables to be changed inside create.py")

Inside ``main.py``, **user_token**,  **user_name**  and **code_editor** have to be adjusted.

![alt Screenshot](https://github.com/lepasq/repo-automation/blob/master/screenshots/batch.png "Path to be changed inside create.bat")

Next, you need to install the required python packages.
```sh
pip3 install -r requirements.txt
```

If your version 3.X of Python is linked to 
`python` instead of `python3`, you should run


```sh
pip install -r requirements.txt
```
and replace the first line of `create.py` with
```sh
#!/usr/bin/env python
```

If you are running windows, you need to replace `echo` inside `create.py` (l. 34) with `ECHO`.


## Add Command to Windows 

In order to use the program inside your command prompt, the folder containing the repository has to be added to the **environment variables.**

In order to open the environment variables, type **env** in the windows search bar and hit enter
Click on **"Environment Variables"**.

Edit the user variable **"Path"** (or create a new user variable with the variable name Path, it if it doesn't exist yet).
Enter the location of the directory containing this repository in the variable name.

Your window should now look like this:

![alt Screenshot](https://github.com/lepasq/repo-automation/blob/master/screenshots/env.png "Environment Variables window")

In order to execute the command, you need to type

```sh
create name
```

 where _name_ is the desired name of the repository that shall be created.

 If you want the command to be called differently, you should change the name of `create.bat`.


## Add Command to Linux 

You should keep the python file `create` in your scripts folder (`~/.local/bin/`) and rename the file to whatever the command should be called.

Finally, you need to add Execution Permissions to your file:

```sh
chmod +x create
```