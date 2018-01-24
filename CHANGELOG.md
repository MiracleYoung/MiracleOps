## version 1.0.2 (2017.01.24)

1. Complete Roster List.
2. Complete Roster Upload.

## version 1.0.1 (2017.01.23)

1. Add Roster model.
2. Add Deploy SSH.
3. Opitimize deploy.js call.

## version 0.5.2 (2017.01.22)

1. Version 1.0.0 release.

## version 0.5.1 (2017.01.22)

1. Add doc app.

## version 0.4.6 (2017.01.22)

1. Complete deploy app v1.
2. Add breadcrumbs nav.

## version 0.4.5 (2017.01.19)

1. Complete MinionRefreshApi, MinionApi.
2. Optimize `asset:server:list`, `asset:server:detail`, `asset:server:update`.
3. Remove `asset:server:create` logic, by salt auto initial.
4. Optimize some layout templates.

## version 0.4.4 (2017.01.19)

1. Optimize MinionRefreshApi: auto fill out server info and create it.
2. Complete deploy.js: deleteMinion, acceptMinion.

## version 0.4.3 (2017.01.18)

1. Add saltapi.py include general salt api by rest-cherrypy.
2. MinionImportApi, MinionCheckAliveApi, MinionApi.
3. salt\_minion\_list.html.

## version 0.4.2 (2017.01.18)

1. Merge entity, server to server.
2. Add SaltMinion model, SaltMinionView.

## version 0.4.1 (2017.01.16)

1. Add deploy app.
2. Update Arch.

## version 0.3.1 (2017.01.15)

1. Change templates using [gentelella](https://github.com/puikinsh/gentelella).
2. Using some days to do research for SaltStack.
3. Version 0.4 will use SaltStack to gather server info, deploy, run command, etc.
4. Need Optimizing Arch to use SaltStack.

## version 0.2.4 (2017.01.12)

1. Complete api: `api-asset:entity-detail`, `api-asset:idc-detail`
2. Complete Server model, api, view.
3. Asset App v1 complete.

**TODO**
1. Bulk export, import.
2. Add Category: Database, Web Service, Middleware, etc.
3. JS optimize.(use React.js)

## version 0.2.3 (2017.01.12)

1. Update `_nav.html` add `<a>` tag to path1.
2. Update Entity model, EntityForm, LoginRequiredMixin.
3. Optimize `entity.html`,`entity_create.html`,`entity_update.html` presentation. 
4. Complete views: `asset:entity:create`, `asset:entity:update`, `asset:entity:delete`, `asset:idc:create`, `asset:idc:update`, `asset:idc:delete`.
5. Add Group model, Update user model add group.

**TODO**
1. `entity, idc delete action`

## version 0.2.2 (2017.01.09)

1. Update IDC, Entity model.
2. Add EntityCreateView, EntityListView, EntityForm, IDCForm.
3. Update root url add `{'app': 'Asset'}`, include url add `{'path1': 'Create'}`
4. Use Datatable to demonstrate ListView.
5. Update Architecture.

**TODO**

1. EntityListView add detail url, action button(edit, delete).
2. EntityDetailView.

## version 0.2.1 (2017.01.09)

1. Add asset module.
2. Add idc templates.
3. Update left side EntityMachine.
4. Add IDC, Server models.

## version 0.1.1 (2017.01.08)

1. Finish User module as below:
- login
- register
- LoginRequiredMixin
2. Official update Project name to MiracleOps.
3. User App v1 complete.

**TODO**

- wechat bound.(notice by wechat)
- Group management.