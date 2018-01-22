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


function importMinions(ele) {
    url = '/api/deploy/minion-refresh/'
    successStr = 'Import Minions Success.'
    salt(ele, url, successStr)
}

function refreshMinionsHealth(ele) {
    url = '/api/deploy/minion-check-alive/'
    successStr = 'Refresh Minions Health Success.'
    salt(ele, url, successStr)
}

// ajax: delete minion
function deleteMinion(ele) {
    var tds = $(ele).parent('td').siblings('td')
    var hostname = tds[0].innerText
    var p = "<p>Hostname:" + hostname + "</p>"
    $('.modal-body').append(p)
    var url = $(ele).parent('td').siblings('input')[0].value
    $('#confirm-delete').attr({"data-delete-url": url})
}

$('#confirm-delete').click(function () {
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
})

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
            $(ele).button('reset')
            window.location.reload()
        }
    }).fail(function (err) {
        alert('Oops, something wrong, please contact your Administrator.')
        $(ele).button('reset')
    })
}