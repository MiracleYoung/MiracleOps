# MiracleOps

[TOC]

## Overview

    This System's BLUEPRINT is to be a Magic Operation System.
    CMDB, Auto-Deployment, Auto-Delivery, Monitor, etc.
    Using SaltStack to do the cluster-management.
    Integrete some others similar system.
    The code is simple, ha.
    You can use it for free, and if you have any idea or question, please contact me.
    
## Architecture

![MiracleOpsArchitecture](https://github.com/MiracleYoung/MiracleOps/raw/master/utils/MiracleOps.png)

## Screenshots

![idc](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/readme/idc.png)

![idc](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/readme/server.png)

![idc](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/readme/server-detail.png)

![idc](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/readme/minion-list.png)

![idc](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/execute_command_server.png)

![idc](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/execute_command_glob.png)

## Installation

1. Please use Python 3.x.(3.6 is recommendation.)
2. Install packages: `pip install -r requirements.txt`
3. Modify MySQL config in MiracleOps.settings.py: 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MiracleOps', # Your Database Name
        # 'HOST': '127.0.0.1',
        'HOST': '192.168.29.134' if 'window' in platform.platform().lower() else '127.0.0.1', # Your MySQL instance host or IP
        'PORT': 3306, # Your MySQL instance port
        'USER': 'root', # Your MySQL instance user
        'PASSWORD': '', # Your MySQL instance password
        'CHARSET': 'utf8', # Your MySQL client character
    }
}
``` 
4. Migrate python data model to MySQL:
```python
python manager.py makemigrations
python manager.py migrate
```
5. Run app in DEBUG schema. `python manager.py runserver 0.0.0.0:8080`
6. Starting development server at `http://0.0.0.0:8080/`

**Important Advice**: Do not use DEBUG schema in production.

If you like it, please star it, and can also join us by QQ, email.

QQ group and email are in the below \#Author.

## Release Notes

### version 1.0.0 (2017.01.22)

- User
    - User Login
    - User Register
- Asset
    - Server
        - Auto initiate Asset by SaltMinion discovery
        - Update Asset
        - Detail Asset
    - IDC
        - Create IDC
        - Update IDC
        - Delete IDC(Just update its status)
        - Detail IDC
- Deploy
    - Minion List
    - Execute Command
    
## Change Logs

[CHANGELOG.md](https://raw.githubusercontent.com/MiracleYoung/MiracleOps/master/CHANGELOG.md)

## TODO List

[TODOLIST.md](https://raw.githubusercontent.com/MiracleYoung/MiracleOps/master/TODOLIST.md)

## Author

**Miracle.Young**

Journey: DBA -> DevOps -> Prince Miracle

Email: miracleyoung0723@gmail.com

QQ Group: 348158993

## Q&A

This is a Miracle(magic) Ops by MiracleYoung.
