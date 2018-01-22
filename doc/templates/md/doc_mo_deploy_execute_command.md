### Server List

#### Button

add: Add one command line and one command argument line.
minus: Minus one command line and one command argument line.

#### Server

This select choice is a muliti-choice widget.

So you can use *ctrl* + *left click* to choose multiple servers.

#### Command & Argument

Use *SaltStack* syntax.

For example:

Command: 
- cmd.run
- disk.usage
- grains.item

Arguments: 
- ls -l /home
- 
- os,username,uuid

**Important**

If one line you have mulitiple arguments, use ',' between two arguments.

#### Snapshot

![Execute Command Server](https://raw.githubusercontent.com/MiracleYoung/MiracleOps/master/static/images/doc/doc_mo_deploy_execute_command_server.png)

### Glob

In this way, you can use glob syntax(like regular but more simple) to retrieve servers.

#### Snapshot

![Execute Command Server](https://raw.githubusercontent.com/MiracleYoung/MiracleOps/master/static/images/doc/doc_mo_deploy_execute_command_glob.png)
