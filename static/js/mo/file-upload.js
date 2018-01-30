Dropzone.autoDiscover = false;


let dropz = new Dropzone("#file-dropzone", {
    url: '/api/deploy/file-upload/',
    uploadMultiple: true,
    maxFiles: 10,
    parallelUploads: 10,
    autoProcessQueue: false,
    sendingmultiple: function (file, xhr, formData) {
        formData.set('glob', $('#reg').val())
        formData.set('dst_dir', $('#dst-dir').val())
    }
})

dropz.on('addedfile', function (file) {
    $('#upload').bind('click', uploadHandle);
});

dropz.on('error', function (file, response, xhr) {
    $(file.previewElement).find('.dz-error-message').text(response);
});

uploadHandle = function () {
    let reg = $('#reg').val()
    let dstDir = $('#dst-dir').val()
    if (!reg || !dstDir) {
        alert('Less glob and destination directory.')
        return
    }
    dropz.processQueue();//开启文件上传
    $('#upload').unbind('click', uploadHandle);

};