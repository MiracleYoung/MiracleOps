function delServer(ele, url, hostname) {
    let modalBody = `<p>Hostname: ${hostname}</p>`
    del(ele, url, modalBody)
}

function delIdc(e) {
    let ele = e.data.ele
    let url = e.data.url
    let idcname = e.data.idcname
    let modalBody = `<p>IDC Name: ${idcname}</p>`
    del(ele, url, modalBody)
}
