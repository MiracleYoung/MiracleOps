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

function importMinions(e) {
    let ele = e.data.ele
    let url = e.data.url
    successStr = 'Import Minions Success.'
    salt(ele, url, successStr)
}

function checkMinionsHealth(e) {
    let ele = e.data.ele
    let url = e.data.url
    successStr = 'Refresh Minions Health Success.'
    salt(ele, url, successStr)
}

// ajax: accept minion key
function acceptMinion(e) {
    var ele = e.data.ele
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
        } else if (err.status == 500) {
            alert('Oops, something wrong, please contact your Administrator.')
        }
    }).always(function () {
        $(ele).button('reset')
        window.location.reload()
    })
}

// delete minion
function delMinion(e) {
    let url = e.data.url
    let hostname = e.data.hostname
    let modalBody = `<p>Please Confirm Your Action: </p> <p>Hostname: ${hostname}</p>`
    del(url, modalBody)
}

// refresh minion button
$('#btn-refresh-minions').on('click', {
    ele: '#btn-refresh-minions',
    url: apiUrl.cm.minionRefresh
}, importMinions)

// check minion alive button
$('#btn-check-minions-health').on('click', {
    ele: '#btn-check-minions-health',
    url: apiUrl.cm.minionCheckAlive
}, checkMinionsHealth)

// delete minion button
$('#a-delete-minion').on('click', {
    url: apiUrl.cm.minion + $('#a-delete-minion').data('id'),
    hostname: $('#a-delete-minion').data('hostname')
}, delMinion)

// accept minion button
$('#btn-accept-minion').on('click', {
    ele: '#btn-accept-minion'
}, acceptMinion)