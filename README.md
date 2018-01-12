# MiracleOps

[TOC]

## Overview

    This System's BLUEPRINT is to be a Magic Operation System.
    CMDB, Auto-Deployment, Auto-Delivery, Monitor, etc.
    
## Architecture

![MiracleOpsArchitecture](https://github.com/MiracleYoung/MiracleOps/raw/master/docs/MiracleOps.png)

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

### version 0.2.4 (2017.01.12)

1. Complete api: `api-asset:entity-detail`, `api-asset:idc-detail`
2. Complete Server model, api, view.
3. Asset App v1 complete.

**TODO**
1. Bulk export, import.
2. Add Category: Database, Web Service, Middleware, etc.
3. JS optimize.(use React.js)

### version 0.2.3 (2017.01.12)

1. Update `_nav.html` add `<a>` tag to path1.
2. Update Entity model, EntityForm, LoginRequiredMixin.
3. Optimize `entity.html`,`entity_create.html`,`entity_update.html` presentation. 
4. Complete views: `asset:entity:create`, `asset:entity:update`, `asset:entity:delete`, `asset:idc:create`, `asset:idc:update`, `asset:idc:delete`.
5. Add Group model, Update user model add group.

**TODO**
1. `entity, idc delete action`

### version 0.2.2 (2017.01.09)

1. Update IDC, Entity model.
2. Add EntityCreateView, EntityListView, EntityForm, IDCForm.
3. Update root url add `{'app': 'Asset'}`, include url add `{'path1': 'Create'}`
4. Use Datatable to demonstrate ListView.
5. Update Architecture.

**TODO**

1. EntityListView add detail url, action button(edit, delete).
2. EntityDetailView.

### version 0.2.1 (2017.01.09)

1. Add asset module.
2. Add idc templates.
3. Update left side EntityMachine.
4. Add IDC, Server models.

### version 0.1.1 (2017.01.08)

1. Finish User module as below:
- login
- register
- LoginRequiredMixin
2. Official update Project name to MiracleOps.
3. User App v1 complete.

**TODO**

- wechat bound.(notice by wechat)
- Group management.

## Author

**Miracle.Young**

Journey: DBA -> DevOps -> Prince Miracle

Email: miracleyoung0723@gmail.com

QQ Group: 348158993

## Q&A

This is a Miracle(magic) Ops by MiracleYoung.

You can use it as free, and if you have any idea or questions, please contact me.

