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

// execute_command.html
$('#tab_server').addClass('active in')

// _glob_exec.html
// bind glob add/minus button
$('#glob-add').on('click', {tab: 'glob'}, add)
$('#glob-minus').on('click', {tab: 'glob'}, minus)
// glob execute button
$('#glob-execute').on('click', {ele: '#glob-execute', url: apiUrl.cm.minionCmd}, globExec)

// _server_exec.html bind glob add/minus button
$('#server-add').on('click', {tab: 'server'}, add)
$('#server-minus').on('click', {tab: 'server'}, minus)
$('#server-execute').on('click', {ele: '#server-execute', url: apiUrl.cm.minionCmd}, serverExec)



// file-upload
Dropzone.autoDiscover = false;

let dropz = new Dropzone("#file-dropzone", {
    url: apiUrl.cm.fileUpload,
    uploadMultiple: true,
    maxFiles: 10,
    parallelUploads: 10,
    autoProcessQueue: false,
    sendingmultiple: function (file, xhr, formData) {
        formData.set('glob', $('#reg').val())
        formData.set('dst_dir', $('#dst-dir').val())
    }
})

dropz.on('addedfile', function (file) {
    $('#upload').bind('click', uploadHandle);
});

dropz.on('error', function (file, response, xhr) {
    $(file.previewElement).find('.dz-error-message').text(response);
});

uploadHandle = function () {
    let reg = $('#reg').val()
    let dstDir = $('#dst-dir').val()
    if (!reg || !dstDir) {
        alert('Less glob and destination directory.')
        return
    }
    dropz.processQueue();//开启文件上传
    $('#upload').unbind('click', uploadHandle);

};



// minion-list
function salt(ele, url, successStr) {
    $.ajax({
            url: url,
            beforeSend: function (xhr) {
                $(ele).button('loading');
            }
        }
    ).done(function (data, status, xhr) {
        alert(successStr)
        $(ele).button('reset')
        window.location.reload(true)
    }).fail(function (err) {
        alert('Oops, something wrong, please contact your administrator.')
        $(ele).button('reset')
    })
}

function importMinions(ele, url) {
    successStr = 'Import Minions Success.'
    salt(ele, url, successStr)
}

function checkMinionsHealth(ele, url) {
    successStr = 'Refresh Minions Health Success.'
    salt(ele, url, successStr)
}

// ajax: accept minion key
function acceptMinion(ele) {
    var url = $(ele).parent('td').siblings('input')[0].value
    $.ajax({
        url: url,
        beforeSend: function (xhr) {
            $(ele).button('loading');
        },
        method: 'PUT'
    }).done(function (data, status, xhr) {
        if (xhr.status == 200) {
            alert('Accept Success.')
        }
    }).fail(function (err) {
        if (err.status == 400) {
            alert('Oops, params error.')
        } else if (err.status == 500){
            alert('Oops, something wrong, please contact your Administrator.')
        }
    }).always(function () {
        $(ele).button('reset')
        window.location.reload()
    })
}

// delete minion
function delMinion(ele, url, hostname) {
    let modalBody = `<p>Hostname: ${hostname}</p>`
    del(ele, url, modalBody)
}

// refresh minion button
$('#btn-refresh-minions').on('click', {ele: '#btn-refresh-minions', url: apiUrl.cm.minionRefresh}, importMinions)

// check minion alive button
$('#btn-check-minions-health').on('click', {ele: '#btn-check-minions-health', url: apiUrl.cm.minionCheckAlive}, checkMinionsHealth)

// delete minion button
$('#a-delete-minion').on('click', {ele: '#a-delete-minion', url: apiUrl.cm.minion}, delMinion(this, "{% url 'api-cm:minion' minion.id %}", "{{ minion.hostname }}"))