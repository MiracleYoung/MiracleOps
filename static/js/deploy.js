// salt_minion_list.html
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


function importMinions(event) {
    successStr = 'Import Minions Success.'
    salt(this, event.data.url, successStr)
}

function refreshMinionsHealth(event) {
    successStr = 'Refresh Minions Health Success.'
    salt(this, event.data.url, successStr)
}

// ajax: delete minion
function deleteMinion() {
    var tds = $(this).parent('td').siblings('td')
    var hostname = tds[0].innerText
    var p = "<p>Hostname:" + hostname + "</p>"
    $('.modal-body').append(p)
    var url = $(this).parent('td').siblings('input')[0].value
    $('#confirm-delete').attr({"data-delete-url": url})
}

function confirmDelete() {
    var url = $(this).attr("data-delete-url")
    $.ajax({
        url: url,
        method: 'DELETE'
    }).done(function (data, status, xhr) {
        if (xhr.status == 204) {
            alert('Delete Success.')
            window.location.reload()
        }
    }).fail(function (err) {
        alert('Oops, something wrong, please contact your Administrator.')
    })
}

// ajax: accept minion key
function acceptMinion() {
    var url = $(this).parent('td').siblings('input')[0].value
    $.ajax({
        url: url,
        beforeSend: function (xhr) {
            $(this).button('loading');
        },
        method: 'PUT'
    }).done(function (data, status, xhr) {
        if (xhr.status == 200) {
            alert('Accept Success.')
            $(this).button('reset')
            window.location.reload()
        }
    }).fail(function (err) {
        alert('Oops, something wrong, please contact your Administrator.')
        $(this).button('reset')
    })
}

//execute_command.html
function execute(event) {
    let tab = event.data.tab
    let tgt_type = event.data.tgt_type
    let url = event.data.url
    let servers = null

    $(`#${tab}-feedback`).empty()

    if (tgt_type == 'glob') {
        servers = $('#reg').val()
    } else if (tgt_type == 'list') {
        servers = []
        for (let s of $('#server').val()) {
            servers.push(s)
        }
    }
    let count = $(`#${tab}-cmd`).data().count
    let cmds = []
    let args = []
    for (let i = 1; i <= count; i++) {
        cmds.push($(`#${tab}-cmd-${i}`).val())
        args.push($(`#${tab}-arg-${i}`).val())
    }

    $.ajax({
        url: url,
        method: 'POST',
        data: {
            servers: servers,
            cmds: cmds,
            args: args,
            type: tgt_type
        }
    }).done(function (data, status, xhr) {
        if (xhr.status == 200) {
            for (let key in data) {
                $(`#${tab}-feedback`).append(`<h4>${key}:</h4>`)
                for (let _key in data[key]) {
                    if (typeof(data[key][_key]) == "object") {
                        $(`#${tab}-feedback`).append(`<p>${_key}: ${JSON.stringify(data[key][_key])}</p>`)
                    } else {
                        $(`#${tab}-feedback`).append(`<p>${_key}: ${data[key][_key]}</p>`)
                    }
                }
            }
        }
    }).fail(function (err) {
        console.log(err)
    })
}

function add(event) {
    $(`#${event.data.tab}-cmd`).data({'count': $(`#${event.data.tab}-cmd`).data().count + 1})
    let count = $(`#${event.data.tab}-cmd`).data('count')
    $(`#${event.data.tab}-cmd`).append(`<input type='text' class='form-group form-control' id='${event.data.tab}-cmd-${count}' />`)
    $(`#${event.data.tab}-arg`).append(`<input type='text' class='form-group form-control' id='${event.data.tab}-arg-${count}' />`)
}

function minus(event) {
    let count = $(`#${event.data.tab}-cmd`).data('count')
    if (count > 1) {
        $(`#${event.data.tab}-cmd-${count}`).remove()
        $(`#${event.data.tab}-arg-${count}`).remove()
        $(`#${event.data.tab}-cmd`).data({'count': count - 1})
    }
}