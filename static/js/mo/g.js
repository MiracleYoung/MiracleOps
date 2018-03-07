// global var
let ws_port = '8002'

// api url route
let apiUrl = {
    prefix: '/api/v1/',
    cms: {},
    assets: {},
    users: {}
}

apiUrl.users.g = apiUrl.prefix + 'users/';
apiUrl.users.login = apiUrl.users.g + 'login/';

apiUrl.cms.g = apiUrl.prefix + 'cms/';
apiUrl.cms.minionRefresh = apiUrl.cms.g + 'minion-refresh/';
apiUrl.cms.minionRefresh = apiUrl.cms.g + 'minion-refresh/';
apiUrl.cms.minionCheckAlive = apiUrl.cms.g + 'minion-check-alive/';
apiUrl.cms.minion = apiUrl.cms.g + 'minion/'; // <id>
apiUrl.cms.minionCmd = apiUrl.cms.g + 'minion-cmd/';
apiUrl.cms.roster = apiUrl.cms.g + 'roster/'; // <id>
apiUrl.cms.installMinion = apiUrl.cms.g + 'install-minion/'; // <roster_id>
apiUrl.cms.sshCmd = apiUrl.cms.g + 'ssh-cmd/';
apiUrl.cms.sls = apiUrl.cms.g + 'sls/'; // <id>
apiUrl.cms.slsCmd = apiUrl.cms.g + 'sls-cmd/';
apiUrl.cms.fileUpload = apiUrl.cms.g + 'file-upload/';

apiUrl.assets.g = apiUrl.prefix + 'assets/';
apiUrl.assets.server = apiUrl.assets.g + 'server/'; //<id>
apiUrl.assets.idc = apiUrl.assets.g + 'idc/'; // <id>


var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
        // ajax add auth header
        if (document.cookie.jwt) {
            xhr.setRequestHeader("ACCESS-TOKEN", document.cookie.jwt);
        }
    }
});

$('body').addClass('nav-md');


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
function del(url, modalBody) {
    $('.modal-body').empty()
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

// execute async feedback
function feedback(data, status, xhr, tab) {
    if (xhr.status == 200) {
        for (let key in data) {
            $(`#${tab}-feedback`).append(`<h4>${key}:</h4>`)
            if (typeof(data[key]) == 'object') {
                for (let _key in data[key]) {
                    if (typeof(data[key][_key]) == "object") {
                        $(`#${tab}-feedback`).append(`<p>${_key}: ${JSON.stringify(data[key][_key])}</p>`)
                    } else {
                        $(`#${tab}-feedback`).append(`<p>${_key}: ${data[key][_key]}</p>`)
                    }
                }
            } else {
                $(`#${tab}-feedback`).append(`<p>${data[key]}</p>`)
            }
        }
    }
}

// button exec
function exec(ele, url, data, tab) {
    $.ajax({
        url: url,
        method: 'POST',
        data: data,
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


// button add
function add(e) {
    let tab = e.data.tab
    $(`#${tab}-cmd`).data({'count': $(`#${tab}-cmd`).data().count + 1})
    let count = $(`#${tab}-cmd`).data('count')
    $(`#${tab}-cmd`).append(`<input type='text' class='form-group form-control' id='${tab}-cmd-${count}' />`)
    $(`#${tab}-arg`).append(`<input type='text' class='form-group form-control' id='${tab}-arg-${count}' />`)
}

// button minus
function minus(e) {
    let tab = e.data.tab
    let count = $(`#${tab}-cmd`).data('count')
    if (count > 1) {
        $(`#${tab}-cmd-${count}`).remove()
        $(`#${tab}-arg-${count}`).remove()
        $(`#${tab}-cmd`).data({'count': count - 1})
    }
}
