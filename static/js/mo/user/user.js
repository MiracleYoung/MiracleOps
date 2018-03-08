function userDetail(uid) {
    $.ajax({
        url: apiUrl.users.userDetail + uid + '/',
        method: 'GET'
    }).done(function (data, status, xhr) {
        Cookies.set(uid, JSON.stringify(data))
        loadUserInfo(uid)
    })
}

function loadUserInfo(uid) {
    let data = JSON.parse(Cookies.get(uid))
    $('.mo-user-name').text(data.name)
    $('.mo-user-avatar').attr('src', data.avatar)
    switch (data.job_title) {
        case 0:
            $('.mo-user-jobtitle').text('Undefined');
            break;
        case 1:
            $('.mo-user-jobtitle').text('Database Administrator');
            break;
        case 2:
            $('.mo-user-jobtitle').text('System Administrator');
            break;
        case 3:
            $('.mo-user-jobtitle').text('Network Administrator');
            break;
        case 4:
            $('.mo-user-jobtitle').text('Help Desk/IT');
            break;
        case 5:
            $('.mo-user-jobtitle').text('Developer');
            break;
        case 6:
            $('.mo-user-jobtitle').text('Tester');
            break;
        case 101:
            $('.mo-user-jobtitle').text('Director');
            break;
        case 102:
            $('.mo-user-jobtitle').text('Manager');
            break;
        case 103:
            $('.mo-user-jobtitle').text('Tech Leader');
            break;
    }
    $('.mo-user-email').text(data.email)

}

