// dropzone
Dropzone.options.slsdropzone = {
    maxFiles: 10,
    maxFilesize: 5120,
    acceptedFiles: '.zip'
}

// sls delete
function delSls(ele, url, fileName) {
    let modalBody = `<p>File Name: ${fileName}</p>`
    del(ele, url, modalBody)
}

// sls execution tab
function slsExec(ele, url) {
    let _sls_id = $('#sls-exec-list').val()
    let tab = 'sls'
    let tgt = $('#reg').val()
    $(`#${tab}-feedback`).empty()
    let data = {
        sls_id: _sls_id,
        tgt: tgt
    }
    exec(ele, url, data, tab)
}