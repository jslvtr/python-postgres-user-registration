# python-postgres-user-registration

This repository is part of the course "The Complete Python/PostgreSQL Developer Course". If you're interested in learning about Python and PostgreSQL, check it out!

## Installing PostgreSQL

To install PostgreSQL easily I would recommend using the installers from EnterpriseDB. The download page is here: https://www.postgresql.org/download/.

## Installing psycopg2

To install the psycopg2 library there are a few ways.

### On UNIX (Linux and Mac OS X)

If you installed PostgreSQL via the EnterpriseDB installer, execute the following commands in a Terminal:

```
export PATH=$PATH:/Library/PostgreSQL/9.5/bin
```

Remember to substitute 9.5 for your PostgreSQL version.

```
pip install --upgrade wheel
pip install --upgrade setuptools
pip install psycopg2
```

### On Windows

On Windows, we first need the Git Bash. Download and install it from here: http://git-for-windows.github.io.

Then, we need to make sure our PATH environment variable contains the appropriate paths.

In your Control Panel, find the System and Security section, and then go into the System section. Here, find the "Advanced System Settings" link, and in there go to the "Advanced" tab. Click on the "Environment Variables" button.

Then, on both the PATH (user variables) and Path (system variables) variables, make sure the following paths have entries:

- `C:\Program Files\PostgreSQL\9.5\bin` (remember to substitute 9.5 for your PostgreSQL version)
- `C:\Users\yourusername\AppData\Local\Programs\Python\Python35-32` (this may be different if you downloaded e.g. Python3.6)

Then, download the psycopg2 installer for your Python version: http://www.stickpeople.com/projects/python/win-psycopg/. Make note of the name of the file you are downloading.

Finally, open up the Git Bash program that we installed initially and execute the following commands:

```
cd ~/Downloads
python -m easy_install <file_name_downloaded>.exe
```

## Running the program

During installation of PostgreSQL, you were prompted for a password.

In the `app.py` file of this repository, make sure your password is present when running the application.

Be careful with putting your passwords up on GitHub!

Modifying the file will **not** publish your password, but if you create your own repository later on, make sure you do not put your passwords in the code. It is not safe.
