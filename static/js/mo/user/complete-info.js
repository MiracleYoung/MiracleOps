function confirm() {
    let username = $('#username').val();
    let wechat = $('#wechat').val();
    let phone = $('#phone').val();
    let avatar = $('#avatar').prop('files')[0];
    let jobtitle = $('#jobtitle').val();

    var formData = new FormData();
    formData.append("avatar", avatar, avatar.name);
    formData.append("name", username);
    formData.append("wechat", wechat);
    formData.append("phone", phone);
    formData.append("job", jobtitle);
    formData.append("code", window.location.pathname.split('/')[3]);

    $.ajax({
        url: apiUrl.users.completeInfo + Cookies.get('uid') + '/',
        method: 'PUT',
        processData: false,
        contentType: false,
        data: formData
    }).done(function (data, status, xhr) {
        if (xhr.status === 200) {
            swal({
                title: 'Congratulation',
                text: 'Personal info completed.',
                type: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
            }).then((result) => {
                window.location = '/users/login/'
            })
        }
    }).fail(function (err) {
        swal(err.responseJSON.msg, '', 'error')
    })
}


function leaveAStepCallback(obj, context) {
    let username = $('#username').val();
    let wechat = $('#wechat').val();
    let phone = $('#phone').val();
    let avatar = $('#avatar').val();
    let jobtitle = $('#jobtitle').val();
    let role = $('#role').val();

    if (context.fromStep === 1) {
        if (!username) {
            swal('Info Error', 'Username is empty.', 'error');
            return false
        }
    }

    if (context.fromStep === 2) {
        if (!wechat) {
            swal('Info Error', 'Wechat is empty.', 'error');
            return false
        }
        if (!phone) {
            swal('Info Error', 'Phone is empty.', 'error');
            return false
        }
    }


    if (context.fromStep === 3) {
        if (!avatar) {
            swal('Info Error', 'Avatar is empty.', 'error');
            return false
        }
        if (!jobtitle) {
            swal('Info Error', 'Jobtitle is empty.', 'error');
            return false
        }
        if (!role) {
            swal('Info Error', 'Role is empty.', 'error');
            return false
        }
        $('#step-4 .form-group').append(`<p>Username: ${username}</p><p>Wechat: ${wechat}</p><p>Phone: ${phone}</p>`)
    }

    return true;
}

function getJobTitle() {
    $.ajax({
        url: apiUrl.users.jobTitles,
        method: 'GET'
    }).done(function (data, status, xhr) {
        if (xhr.status === 200) {
            for (let job of data) {
                $('#jobtitle').append(`<option value="${job.id}">${job.name}</option>`)
            }
        }
    }).fail(function (err) {
        console.log(err)
    })
}

function getRoles() {
    $.ajax({
        url: apiUrl.users.roles,
        method: 'GET'
    }).done(function (data, status, xhr) {
        if (xhr.status === 200) {
            for (let role of data) {
                $('#role').append(`<option value="${role.id}">${role.name}</option>`)
            }
        }
    }).fail(function (err) {
        console.log(err)
    })
}

getJobTitle()
getRoles()

$('#wizard').smartWizard({
    onLeaveStep: leaveAStepCallback,
    onFinish: confirm
});
