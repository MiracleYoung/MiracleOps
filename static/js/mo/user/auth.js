function login() {
    let email = $('#mo-login-email').val()
    let password = $('#mo-login-password').val()
    $.ajax({
        url: apiUrl.users.login,
        data: {email: email, password: password},
        method: 'POST'
    }).done(function (data, status, xhr) {
        if (xhr.status === 200) {
            swal({
                title: data.msg,
                type: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
            }).then((result) => {
                window.location = data.data.url
            })
        }
    }).fail(function (err) {
        if ([451, 452].includes(err.status)) {
            swal('Login Failed', err.responseJSON.msg, 'error')
        }
    })
}

function register() {
    let email = $('#mo-register-email').val()
    let password = $('#mo-register-password').val()
    let password2 = $('#mo-register-password2').val()
    if (password !== password2) {
        swal('Password are different. Please confirm.', '', 'error')
        return
    }
    $.ajax({
        url: apiUrl.users.register,
        data: {email: email, password: password},
        method: 'POST'
    }).done(function (data, status, xhr) {
        if (xhr.status === 200) {
            swal({
                title: data.msg,
                type: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
            }).then((result) => {
                window.location = data.data.url
            })
        }
    }).fail(function (err) {
        if ([454].includes(err.status)) {
            swal(err.responseJSON.msg, '', 'error')
        }
    })
}

$('#mo-login-login').on('click', login)

$('#mo-register-register').on('click', register)

