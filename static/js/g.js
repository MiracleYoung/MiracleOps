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
function del(ele, url, modalBody) {
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