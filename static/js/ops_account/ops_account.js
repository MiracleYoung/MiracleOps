/**
 * Created by miracleYoung on 2017/7/26.
 */

function resetPassword() {
    let email = $('#email').val()
    $.ajax({
        beforeSend: function (xhr) {
            $('#notice').addClass('hidden')
            $('#btn-account-reset').addClass('disabled').attr({disabled: 'true'})
        },
        url: '/account/reset_password',
        dataType: 'json',
        method: 'GET',
        data: {email: email}
    }).done(function (data, status, xhr) {
        $('#message').html(data['message'])
        $('#notice').removeClass('hidden')
        $('#btn-account-reset').removeAttr('disabled').removeClass('disabled')
    }).fail(function (xhr, status, err) {
        $('#message').html(xhr['message'])
    })
}

$('#btn-account-reset').click(function () {
    resetPassword()
})