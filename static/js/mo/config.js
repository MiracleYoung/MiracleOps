// global var
let ws_port = '8002'

// api url route
let apiUrl = {
    prefix: '/api/v1/',
    cms: {},
    assets: {},
    users: {}
}

apiUrl.users.g = apiUrl.prefix + 'user/';
apiUrl.users.login = apiUrl.users.g + 'login/';
apiUrl.users.userDetail = apiUrl.users.g;

apiUrl.cms.g = apiUrl.prefix + 'cms/';
apiUrl.cms.minionRefresh = apiUrl.cms.g + 'minion-refresh/';
apiUrl.cms.minionRefresh = apiUrl.cms.g + 'minion-refresh/';
apiUrl.cms.minionCheckAlive = apiUrl.cms.g + 'minion-check-alive/';
apiUrl.cms.minion = apiUrl.cms.g + 'minion/'; // <id>
apiUrl.cms.minionCmd = apiUrl.cms.g + 'minion-cmd/';
apiUrl.cms.roster = apiUrl.cms.g + 'roster/'; // <id>
apiUrl.cms.installMinion = apiUrl.cms.g + 'install-minion/'; // <roster_id>
apiUrl.cms.sshCmd = apiUrl.cms.g + 'ssh-cmd/';
apiUrl.cms.sls = apiUrl.cms.g + 'sls/'; // <id>
apiUrl.cms.slsCmd = apiUrl.cms.g + 'sls-cmd/';
apiUrl.cms.fileUpload = apiUrl.cms.g + 'file-upload/';

apiUrl.assets.g = apiUrl.prefix + 'assets/';
apiUrl.assets.server = apiUrl.assets.g + 'server/'; //<id>
apiUrl.assets.idc = apiUrl.assets.g + 'idc/'; // <id>