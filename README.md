# MiracleOps

[TOC]

## Overview

    This System's BLUEPRINT is to be a Magic Operation System.
    CMDB, Auto-Deployment, Auto-Delivery, Monitor, etc.
    
## Architecture

![MiracleOpsArchitecture](https://github.com/MiracleYoung/MiracleOps/raw/master/docs/MiracleOps.png)

## Release Notes

### version 0.2.4 (2017.01.12)

1. Complete api: `api-asset:entity-detail`, `api-asset:idc-detail`

**Asset module simple complete.**

**TODO**
1. Bulk export, import.
2. JS optimize.

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

**TODO**

- wechat bound.(notice by wechat)
- Group management.

## Author

**Miracle.Young**

Journey: DBA -> DevOps -> Prince Miracle

Email: miracleyoung0723@gmail.com

## Q&A

This is a Miracle(magic) Ops by MiracleYoung.

You can use it as free, and if you have any idea or questions, please contact me.

