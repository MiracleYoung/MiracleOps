// exec-cmd
function minionExec(ele, url, servers, tab, tgt_type) {
    $(`#${tab}-feedback`).empty()
    let count = $(`#${tab}-cmd`).data().count
    let cmds = []
    let args = []
    for (let i = 1; i <= count; i++) {
        cmds.push($(`#${tab}-cmd-${i}`).val())
        args.push($(`#${tab}-arg-${i}`).val())
    }
    let data = {
        servers: servers,
        cmds: cmds,
        args: args,
        type: tgt_type
    }
    exec(ele, url, data, tab)
}

function serverExec(e) {
    let ele = e.data.ele
    let url = e.data.url
    let tab = 'server'
    let tgt_type = 'list'
    let servers = []
    for (let s of $('#server').val()) {
        servers.push(s)
    }
    minionExec(ele, url, servers, tab, tgt_type)
}

function globExec(e) {
    let ele = e.data.ele
    let url = e.data.url
    let tab = 'glob'
    let tgt_type = 'glob'
    let servers = $('#reg').val()
    minionExec(ele, url, servers, tab, tgt_type)
}

$('#tab_server').addClass('active in')

// glob execute button
$('#glob-execute').on('click', {ele: '#glob-execute', url: apiUrl.cm.minionCmd}, globExec)
$('#server-execute').on('click', {ele: '#server-execute', url: apiUrl.cm.minionCmd}, serverExec)