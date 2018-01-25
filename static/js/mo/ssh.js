// salt_ssh.html
// dropzone
Dropzone.options.filedropzone = {
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
function installMinion(ele, tab) {
    let _pk = $('#roster-install-list').val()
    $.ajax({
        url: `/api/deploy/install-minion/${_pk}/`,
        method: 'GET',
        beforeSend: function () {
            $(ele).button('loading')
        }
    }).done(function (data, status, xhr) {
        feedback(data, status, xhr, tab)
        $(ele).button('reset')
    })
}

// roster execution tab
function rosterExec(ele) {
    let _roster_id = $('#roster-exec-list').val()
    let url = '/api/deploy/ssh-cmd/' + _roster_id + '/'
    let tab = 'roster'
    $(`#${tab}-feedback`).empty()
    let cmds = $(`#${tab}-cmd-1`).val()
    let args = $(`#${tab}-arg-1`).val()
    let data = {
        cmds: cmds,
        args: args
    }
    exec(ele, url, data, tab)
}
