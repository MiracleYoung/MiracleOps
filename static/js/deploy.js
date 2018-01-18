function salt(ele, url, successStr){
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


function importMinions(ele) {
    url= '/api/deploy/minion-import/'
    successStr = 'Import Minions Success.'
    salt(ele, url, successStr)
}

function refreshMinionsHealth(ele) {
    url= '/api/deploy/minion-check-alive/'
    successStr = 'Refresh Minions Health Success.'
    salt(ele, url, successStr)
}

function deleteMinion(ele) {
    var tds = $(ele).parent('td').siblings('td')
    var item = []
    for (var i = 0; i < tds.length; i++) {
        item.push(tds[i].innerText)
    }
    var p = "<p>Hostname:" + item[0] + "</p>"
    $('.modal-body').append(p)
    $('#confirm-delete').attr({"data-delete-url": item[0]})
}

$('#confirm-delete').click(function () {
    var hostname = $(this).attr("data-delete-url")
    var url = $(this).attr("data-delete-url")
    $.ajax({
        url: url,
        data: {
            'hostname': hostname
        },
        method: 'DELETE'
    }).done(function (data, status, xhr) {
        if (xhr.status == 204) {
            alert('Delete Success.')
            window.location.reload()
        }
    }).fail(function (err) {
        alert('Oops, something wrong, please contact your Administrator.')
    })
})

function acceptMinion(ele) {
    var tds = $(ele).parent('td').siblings('td')
    var hostname = tds[0].innerText
    var url = $(ele).parent('td').siblings('input')[0].value

    $.ajax({
        url: url,
        method: 'PUT',
        data: {
            'hostname': hostname
        }
    }).done(function (data, status, xhr) {
        if (xhr.status == 200) {
            alert('Delete Success.')
            window.location.reload()
        }
    }).fail(function (err) {
        alert('Oops, something wrong, please contact your Administrator.')
    })
}