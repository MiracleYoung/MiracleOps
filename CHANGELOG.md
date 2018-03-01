## version 1.4.1 (2018.03.01)
1. Change partial htmljs to js. Ready to do front-backend separation.
2. Change js files directory.

## version 1.4 release (2018.02.08)
1. Fix bugs.
2. Complete *Terminal* module.
3. Add *Terminal* doc.
4. Update Arch.

## version 1.3.4 (2018.02.08)
1. Fix bugs.
2. `terminal:list` rc.

## version 1.3.3 (2018.02.07)
1. Fix bugs.
2. Update all models' id from auto_increment to uuid.
3. Do `terminal:list`.

## version 1.3.2 (2018.02.07)
1. Fix bugs.
2. Go through the webssh data.

## version 1.3.1 (2018.02.01)
1. Fix bugs.
2. Change *Deploy* app to *CM* app.

## version 1.3 release (2018.01.31)
1. Optimize *File Upload*.
2. Fix *SSH* bugs.
3. Add *File Upload* doc.

## version 1.2.2 (2018.01.30)
1. Complete *File Upload*.

## version 1.2.1 (2018.01.29)
1. Add *File Upload* unit.

## version 1.2 release (2018.01.27)
1. Complete *SLSApi*, *SLSCmdApi*, *SaltSLSView*.
2. Add `sls.js`.
3. Fix some Bugs.
4. Add *SLS* doc.
5. Change *Doc* structure. Update `.html` to `.md` for detail docs.

## version 1.1.1 (2018.01.26)
1. Add *SLSApi*, *SaltSLSView* and related templates.
2. Add *SLS* model.

## version 1.1 release (2018.01.25)
1. Complete SSH unit.
2. Opitmize `g.js`, `ssh.js`, `execute-command.js`, `salt-minion-list.js`.
3. Fix some bugs.
4. Improve installation step.
5. Update Arch.
6. Add *SSH* doc.

## version 1.0.3.2 (2018.01.25)
1. Split deploy.js to `ssh.js`, `execute-command.js`, `salt-minion-list.js`.
2. Add *InstallMinionApi*, *SSHCmdApi*.

## version 1.0.3.1 (2018.01.24)
1. Optimize `asset.js`, `ssh.js`.
2. Complete *RosterApi*.

## version 1.0.2 (2018.01.24)
1. Complete *Roster List*, *Roster Upload*.

## version 1.0.1 (2018.01.23)
1. Add *Roster* model.
2. Add *Deploy SSH*.
3. Opitimize `ssh.js` call.

## version 1.0 release (2018.01.22)
1. Add *Asset Doc*.
2. Add *Salt Minion Execution*, *Salt Minion List* doc. 

## version 0.5.1 (2018.01.22)
1. Add *doc* app.

## version 0.4.6 (2018.01.22)
1. Complete *deploy* app v1.
2. Add breadcrumbs nav.

## version 0.4.5 (2018.01.19)
1. Complete *MinionRefreshApi*, *MinionApi().
2. Optimize `asset:server:list`, `asset:server:detail`, `asset:server:update`.
3. Remove `asset:server:create` logic, by salt auto initial.
4. Optimize some layout templates.

## version 0.4.4 (2018.01.19)
1. Optimize *MinionRefreshApi*: auto fill out server info and create it.
2. Complete `ssh.js`: *deleteMinion*, *acceptMinion*.

## version 0.4.3 (2018.01.18)
1. Add `saltapi.py` include general salt api by `rest-cherrypy`.
2. *MinionImportApi*, *MinionCheckAliveApi*, *MinionApi*.
3. `salt_minion_list.html`.

## version 0.4.2 (2018.01.18)
1. Merge *entity*, *server* to server.
2. Add *SaltMinion* model, *SaltMinionView*.

## version 0.4.1 (2018.01.16)
1. Add *deploy* app.
2. Update Arch.

## version 0.3.1 (2018.01.15)
1. Change templates using [gentelella](https://github.com/puikinsh/gentelella).
2. Using some days to do research for SaltStack.
3. Version 0.4 will use SaltStack to gather server info, deploy, run command, etc.
4. Need Optimizing Arch to use SaltStack.

## version 0.2.4 (2018.01.12)
1. Complete api: `api-asset:entity-detail`, `api-asset:idc-detail`
2. Complete Server model, api, view.
3. Asset App v1 complete.

**TODO**
1. Bulk export, import.
2. Add Category: Database, Web Service, Middleware, etc.
3. JS optimize.(use React.js)

## version 0.2.3 (2018.01.12)
1. Update `_nav.html` add `<a>` tag to path1.
2. Update Entity model, EntityForm, LoginRequiredMixin.
3. Optimize `entity.html`,`entity_create.html`,`entity_update.html` presentation. 
4. Complete views: `asset:entity:create`, `asset:entity:update`, `asset:entity:delete`, `asset:idc:create`, `asset:idc:update`, `asset:idc:delete`.
5. Add Group model, Update user model add group.

**TODO**
1. `entity, idc delete action`

## version 0.2.2 (2018.01.09)
1. Update IDC, Entity model.
2. Add EntityCreateView, EntityListView, EntityForm, IDCForm.
3. Update root url add `{'app': 'Asset'}`, include url add `{'path1': 'Create'}`
4. Use Datatable to demonstrate ListView.
5. Update Architecture.

**TODO**

1. EntityListView add detail url, action button(edit, delete).
2. EntityDetailView.

## version 0.2.1 (2018.01.09)
1. Add asset module.
2. Add idc templates.
3. Update left side EntityMachine.
4. Add IDC, Server models.

## version 0.1.1 (2018.01.08)
1. Finish User module as below:
- login
- register
- LoginRequiredMixin
2. Official update Project name to MiracleOps.
3. User App v1 complete.

**TODO**

- wechat bound.(notice by wechat)
- Group management.