function delServer(ele, url, hostname) {
    let modalBody = `<p>Hostname: ${hostname}</p>`
    del(ele, url, modalBody)
}

function delIdc(ele, url, idcname) {
    let modalBody = `<p>IDC Name: ${idcname}</p>`
    del(ele, url, modalBody)
}

$('#confirm-delete').click(confirmDel)