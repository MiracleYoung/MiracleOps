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
function installMinion(ele, tab) {
    $(`#${tab}-feedback`).empty()
    let _pk = $('#roster-install-list').val()
    $.ajax({
        url: `/api/cm/install-minion/${_pk}/`,
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
function rosterExec(ele, url) {
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
