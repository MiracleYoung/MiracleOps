function login() {
    let email = $('#email').val()
    let password = $('#password').val()
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
            swal(data.msg, '', 'error')
        }
    })
}

$('#login').on('click', login)