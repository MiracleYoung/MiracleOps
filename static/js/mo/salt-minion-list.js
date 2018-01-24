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
