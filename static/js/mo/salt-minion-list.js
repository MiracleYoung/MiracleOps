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

function importMinions(ele, url) {
    successStr = 'Import Minions Success.'
    salt(ele, url, successStr)
}

function refreshMinionsHealth(ele, url) {
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