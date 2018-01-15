// $('#table-list').dataTable()

function setValue(e) {
    var tds = $(e).parent('td').siblings('td')
    var item = []
    for (var i = 0; i < tds.length; i++) {
        item.push(tds[i].innerText)
    }
    var p = "<p>SN:" + item[0] + "</p>"
    $('.modal-body').append(p)
    var deleteUrl = $(e).parent('td').siblings('input')[0].value
    $('#confirm-delete').attr({"data-delete-url": deleteUrl})
}

$('#confirm-delete').click(function () {
    var deleteUrl = $(this).attr("data-delete-url")
    var listUrl = $(this).attr("data-list-url")
    $.ajax({
        url: deleteUrl,
        method: 'DELETE'
    }).done(function (data, status, xhr) {
        if (xhr.status == 204) {
            alert('Delete Success.')
            window.location.href = listUrl
        }
    }).fail(function (err) {
        alert('Oops, something wrong, please contact your Administrator.')
    })
})