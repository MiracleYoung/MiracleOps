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

![server](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/server.png)

#### Salt Minion

![minion-list](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/minion-list.png)

![execute_command_server](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/execute_command_server.png)

#### Salt SSH

![ssh install minion](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/ssh_install_minion.png)

![ssh cmd](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/ssh_cmd.png)

#### Salt SLS

![sls list](https://github.com/MiracleYoung/MiracleOps/raw/master/static/images/doc/mo/sls_list.png)

## Installation

[Install Manual](https://github.com/MiracleYoung/MiracleOps/raw/master/utils/INSTALL_MANUAL.md)

**Important Advice**: Do not use DEBUG schema in production.

If you like it, please star it, and can also join us by QQ, email.

QQ group and email are in the below [#Author](https://github.com/MiracleYoung/MiracleOps#author).

## Features

- User
    - Login
    - Register
- Asset
    - Server
        - Auto initiate server by salt-minion discovery
        - Update/Detail server
    - IDC
        - Create/Update/Delete/Detail IDC
- Deploy
    - Minion List
        - Refresh minion
        - Check minion health
    - Execute Command
        - Choose Server List
        - Use glob expression
    - SSH
        - Roster list/detail
        - Upload roster
        - Install salt-minion
        - Execute Command by SSH
    - SLS
        - SLS List/detail
        - Upload sls
        - Apply sls
    - File
        - Upload
    
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
