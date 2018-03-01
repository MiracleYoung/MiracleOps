// salt_ssh.html

// dropzone
Dropzone.options.rosterdropzone = {
    maxFiles: 10,
    maxFilesize: 5120,
    acceptedFiles: ".roster"
}

// button delete roster
function delRoster(ele, url, fileName) {
    let modalBody = `<p>File Name: ${fileName}</p>`
    del(ele, url, modalBody)
}


// button install minion
function installMinion(e) {
    let ele = e.data.ele
    let tab = e.data.tab
    $(`#${tab}-feedback`).empty()
    let _pk = $('#roster-install-list').val()
    $.ajax({
        url: apiUrl.cm.installMinion + _pk + '/',
        method: 'GET',
        beforeSend: function () {
            $(ele).button('loading')
        }
    }).done(function (data, status, xhr) {
        feedback(data, status, xhr, tab)
    }).fail(function (err) {

    }).always(function () {
        $(ele).button('reset')
    })
}

// roster execution tab
function rosterExec(e) {
    let ele = e.data.ele
    let url = e.data.url
    let _roster_id = $('#roster-exec-list').val()
    let tab = 'roster'
    $(`#${tab}-feedback`).empty()
    let cmds = $(`#${tab}-cmd-1`).val()
    let args = $(`#${tab}-arg-1`).val()
    let data = {
        roster_id: _roster_id,
        cmds: cmds,
        args: args
    }
    exec(ele, url, data, tab)
}


// ssh install minion button
$('#minion-install').on('click', {
    ele: '#minion-install',
    tab: 'install'
}, installMinion)

// roster execute button
$('#roster-execute').on('click', {
    ele: '#roster-execute',
    url: apiUrl.cm.sshCmd
}, rosterExec)