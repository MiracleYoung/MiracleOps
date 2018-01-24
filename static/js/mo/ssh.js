// salt_ssh.html
// button delete roster
function delRoster(ele, url, fileName) {
    let modalBody = `<p>File Name: ${fileName}</p>`
    del(ele, url, modalBody)
}


// button install minion
function installMinion(event) {
    let _tab = event.data.tab
    let _pk = $('#roster-install-list').val()
    $.ajax({
        url: `/api/deploy/install-minion/${_pk}/`,
        method: 'GET'
    }).done(function (data, status, xhr) {
        if (xhr.status == 200) {
            for (let key in data) {
                $(`#${_tab}-feedback`).append(`<h4>${key}:</h4>`)
                if (typeof(data[key]) == 'object') {
                    for (let _key in data[key]) {
                        if (typeof(data[key][_key]) == "object") {
                            $(`#${_tab}-feedback`).append(`<p>${_key}: ${JSON.stringify(data[key][_key])}</p>`)
                        } else {
                            $(`#${_tab}-feedback`).append(`<p>${_key}: ${data[key][_key]}</p>`)
                        }
                    }
                } else {
                    $(`#${_tab}-feedback`).append(`<p>${data[key]}</p>`)
                }
            }
        }
    })
}



