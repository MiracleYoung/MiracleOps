// execute_command.html
$('#tab_server').addClass('active in')

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

function serverExec(ele, url) {
    let tab = 'server'
    let tgt_type = 'list'
    let servers = []
    for (let s of $('#server').val()) {
        servers.push(s)
    }
    minionExec(ele, url, servers, tab, tgt_type)
}

function globExec(ele, url) {
    let tab = 'glob'
    let tgt_type = 'glob'
    let servers = $('#reg').val()
    minionExec(ele, url, servers, tab, tgt_type)
}