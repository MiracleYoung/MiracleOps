// _modal_detail.html
function checkDetail(ele, url) {
    $('.modal-title').empty()
    $('.modal-body').empty()
    let _title = $(ele).text()
    $.ajax({
        url: url,
        method: 'GET'
    }).done(function (data, status, xhr) {
        if (xhr.status == 200) {
            $('.modal-title').html(_title)
            $('.modal-body').html(data)
        }
    })
}

// _modal_delete.html
function del(ele, url, modalBody) {
    $('.modal-body').append(modalBody)
    $('#confirm-delete').data({"del-url": url})
}

function confirmDel() {
    var delUrl = $('#confirm-delete').data("del-url")
    $.ajax({
        url: delUrl,
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

// button execute
function execute(ele, url, tab, tgt_type) {
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

// button add
function add(ele, tab) {
    $(`#${tab}-cmd`).data({'count': $(`#${tab}-cmd`).data().count + 1})
    let count = $(`#${tab}-cmd`).data('count')
    $(`#${tab}-cmd`).append(`<input type='text' class='form-group form-control' id='${tab}-cmd-${count}' />`)
    $(`#${tab}-arg`).append(`<input type='text' class='form-group form-control' id='${tab}-arg-${count}' />`)
}

// button minus
function minus(event) {
    let count = $(`#${tab}-cmd`).data('count')
    if (count > 1) {
        $(`#${tab}-cmd-${count}`).remove()
        $(`#${tab}-arg-${count}`).remove()
        $(`#${tab}-cmd`).data({'count': count - 1})
    }
}
