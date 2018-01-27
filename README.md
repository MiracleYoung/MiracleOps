# MiracleOps

[TOC]

## Overview

    This System's BLUEPRINT is to be a Magic Operation System.
    CMDB, Auto-Deployment, Auto-Delivery, Monitor, etc.
    Using SaltStack to do the cluster-management.
    Integrete some others similar system.
    The code is simple, ha.
    MiracleOps has its own manual in left sidebar, name doc.
    You can use it for free, and if you have any idea or question, please contact me.
    
    
## Architecture

![MiracleOpsArchitecture](https://github.com/MiracleYoung/MiracleOps/raw/master/utils/MiracleOps.png)

## Screenshots

#### Asset:

![idc](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/idc.png)

![server](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/server.png)

![server-detail](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/server-detail.png)

#### Salt Minion

![minion-list](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/minion-list.png)

![execute_command_server](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/execute_command_server.png)

![execute_command_glob](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/execute_command_glob.png)

#### Salt SSH

![ssh roster list detail](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/ssh_roster_list_detail.png)

![ssh roster upload](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/ssh_roster_upload.png)

![ssh install minion](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/ssh_install_minion.png)

![ssh cmd](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/ssh_cmd.png)

#### Salt SLS

![sls list](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/sls_list.png)

![sls upload](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/sls_upload.png)

![sls upload structure](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/sls_upload_structure.png)

## Installation

### Salt & Salt-Api

1. Install salt-master on your master server

**PS**: Recommend Python 2.7 on master server, although SaltStack have been compatibile to Python 3, actually not very well in my side.
```bash
curl -L https://bootstrap.saltstack.com -o install_salt.sh
sudo sh install_salt.sh -M
```

2. If you want to install salt-minion, do below script on your minion server

**PS**: After v1.1, MO supply SSH module to installed minion on web
```bash
curl -L https://bootstrap.saltstack.com -o install_salt.sh
sudo sh install_salt.sh
```

3. Install salt-api, salt python packages.
```bash
pip install salt salt-api
```

4. Write the following content to your master config, ex: `/etc/salt/master.d/salt-api.conf`
```yaml
interface: 0.0.0.0

external_auth:
  pam:
    saltapi:
      - .*
      - '@wheel'
      - '@runner'
      - '@jobs'

rest_cherrypy:
  port: 9000
  disable_ssl: True # disable ssl for simple
```

5. In order to make sure your salt-api work, create a *saltapi* user on your master server for *salt rest api* auth.
```bash
pip install rest_cherrypy # supply rest api
useradd saltapi -s /sbin/nologin
```

6. Test your salt-api
```bash
[root@miracle salt]# salt-api exec

# open another terminal
[root@miracle salt]# curl http://localhost:9000/login \
>     -H 'Accept: application/x-yaml' \
>     -d username=saltapi \
>     -d password=saltapi \
>     -d eauth=pam
return:
- eauth: pam
  expire: 1516793480.405034
  perms:
  - .*
  - '@wheel'
  - '@runner'
  - '@jobs'
  start: 1516750280.405032
  token: 3bfe295499a6702d2de00b4f93bde66509de8d31
  user: saltapi
```
This means you already installed successfully!

### Web

1. Please use Python 3.x.(3.6 is recommendation.)
2. Install packages: `pip install -r requirements.txt`
3. Modify MySQL config in MiracleOps.settings.py: 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MiracleOps', # Your Database Name
        # 'HOST': '127.0.0.1',
        'HOST': '127.0.0.1', # Your MySQL instance host or IP
        'PORT': 3306, # Your MySQL instance port
        'USER': 'root', # Your MySQL instance user
        'PASSWORD': '', # Your MySQL instance password
        'CHARSET': 'utf8', # Your MySQL client character
    }
}

SALT_API_URL = 'http://127.0.0.1:9000' # change it to your salt-api host:port
SALT_API_USERNAME = 'saltapi' # your saltapi user 
SALT_API_PASSWORD = 'saltapi'
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

### version 1.1 release (2018.01.25)

1. Complete SSH unit.
2. Opitmize js.
3. Fix some bugs.
4. Improve installation step.
5. Update Arch.

### version 1.0 release (2018git .01.22)

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
