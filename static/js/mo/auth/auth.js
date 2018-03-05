function login() {
    let email = $('#email').val()
    let password = $('#password').val()
    $.ajax({
        url: apiUrl.users.login,
        data: {email: email, password: password},
        method: 'POST'
    }).done(function (data, status, xhr) {
        if (data.code == 200) {
            swal({
                title: data.msg,
                type: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
            }).then((result) => {
                window.location = '/'
            })
        } else if (data.code == 404) {
            swal({
                title: data.msg,
                type: 'error',
                showCancelButton: false,
                confirmButtonColor: '#d33',
            })
        }
    })
}

$('#login').on('click', login)