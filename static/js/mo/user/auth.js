function login() {
    let email = $('#mo-login-email').val()
    let password = $('#mo-login-password').val()
    $.ajax({
        url: apiUrl.users.login,
        data: {email: email, password: password},
        method: 'POST'
    }).done(function (data, status, xhr) {
        if (data.code == 0) {
            swal({
                title: data.msg,
                type: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
            }).then((result) => {
                window.location = data.data.url
            })
        } else if ([1001, 1002].includes(data.code)) {
            swal('Login Failed', data.msg, 'error')
        }
    }).fail(function (err) {
        console.log(err)
    })
}

function register() {
    let email = $('#mo-register-email').val()
    let password = $('#mo-register-password').val()
    let password2 = $('#mo-register-password2').val()
    if (password !== password2){
        swal('Password are different. Please confirm.', '', 'error')
        return
    }
    $.ajax({
        url: apiUrl.users.register,
        data: {email: email, password: password},
        method: 'POST'
    }).done(function (data, status, xhr) {
        if (data.code == 0) {
            swal({
                title: data.msg,
                type: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
            }).then((result) => {
                window.location = data.data.url
            })
        } else if ([1004].includes(data.code)) {
            swal(data.msg, '', 'error')
        }
    }).fail(function (err) {
        swal('Oops, something wrong with server.', '', 'error')
    })
}

$('#mo-login-login').on('click', login)

$('#mo-register-register').on('click', register)

