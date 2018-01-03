/**
 * Created by miracleYoung on 2017/7/27.
 */

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


// validate server create
function validateIp() {
    if (!$('#server-ip').val()) {
        $('#server-modal-body').append("<p>server ip can not be null.</p>")
        return 0
    }
    return true
}

function validateHostname() {
    if (!$('#server-hostname').val()) {
        $('#server-modal-body').append("<p>server hostname can not be null.</p>")
        return 0
    }
    return true
}

function validateIdc() {
    if (!$('#server-idc').val()) {
        $('#server-modal-body').append("<p>server idc can not be null.</p>")
        return 0
    }
    return true
}

function validateCabinet() {
    if (!$('#server-cabinet').val()) {
        $('#server-modal-body').append("<p>server cabinet can not be null.</p>")
        return 0
    }
    return true
}

function validateCabinetUnit() {
    if (!$('#server-cabinet-unit').val()) {
        $('#server-modal-body').append("<p>server cabinet unit can not be null.</p>")
        return 0
    }
    return true
}

function validateSwitch1() {
    if (!$('#server-switch1').val()) {
        $('#server-modal-body').append("<p>server switch1 can not be null.</p>")
        return 0
    }
    return true
}

function validateSwitch1Port() {
    if (!$('#server-switch1-port').val()) {
        $('#server-modal-body').append("<p>server switch1 port can not be null.</p>")
        return 0
    }
    return true
}

function validateSwitch2() {
    if (!$('#server-switch2').val()) {
        $('#server-modal-body').append("<p>server switch2 can not be null.</p>")
        return 0
    }
    return true
}

function validateSwitch2Port() {
    if (!$('#server-switch2-port').val()) {
        $('#server-modal-body').append("<p>server switch2 port can not be null.</p>")
        return 0
    }
    return true
}

function validateMgr() {
    if (!$('#server-mgr').val()) {
        $('#server-modal-body').append("<p>server mgr can not be null.</p>")
        return 0
    }
    return true
}

function validateMgrPort() {
    if (!$('#server-mgr-port').val()) {
        $('#server-modal-body').append("<p>server mgr port can not be null.</p>")
        return 0
    }
    return true
}

// submit server create form
function submitServerForm() {
    $('#server-modal-body').empty()
    if ((validateIp() + validateHostname() + validateIdc() + validateCabinet() + validateCabinetUnit()
        + validateSwitch1() + validateSwitch1Port() + validateSwitch2() + validateSwitch2Port()
        + validateMgr() + validateMgrPort()) === 0) {
        return false
    }
    $.ajax({
        beforeSend: function(xhr, settings){
            var csrftoken = Cookies.get('csrftoken')
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
        },
        url: '/cmdb/create_server/',
        dataType: 'json',
        method: 'POST',
        data: {
            'server-ip': $('#server-ip').val(),
            'server-hostname': $('#server-hostname').val(),
            'server-project': $('#server-project').val(),
            'server-idc': $('#server-idc').val(),
            'server-cabinet': $('#server-cabinet').val(),
            'server-cabinet-unit': $('#server-cabinet-unit').val(),
            'server-switch1': $('#server-switch1').val(),
            'server-switch1-port': $('#server-switch1-port').val(),
            'server-switch2': $('#server-switch2').val(),
            'server-switch2-port': $('#server-switch2-port').val(),
            'server-mgr': $('#server-mgr').val(),
            'server-mgr-port': $('#server-mgr-port').val()
        }
    }).done(function (data) {
        $('#server-modal-body').append("<p>Create server success. Your server is:</p>")
        $('#server-modal-body').append("<p>" + data.ip + "</p>")
    }).fail(function (err) {
        $('#server-modal-body').append("<p>" + err.message + "</p>")
    })

}

function getIdc() {
    $.ajax({
        url: '/cmdb/get_idc/',
        method: 'GET',
    }).done(function (data) {
        idc = JSON.parse(data)
        for (var i = 0; i < idc.length; i++) {
            $('#server-idc').append("<option>" + idc[i] + "</option>")
        }

    })
}


