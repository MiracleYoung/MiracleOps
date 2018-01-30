Dropzone.autoDiscover = false;

let dropz = new Dropzone("#file-dropzone", {
    url: '/api/deploy/file-upload/',
    uploadMultiple: true,
    parallelUploads: 5,
    autoProcessQueue: false,
    sendingmultiple: function (file, xhr, formData) {
        formData.set('glob', $('#reg').val())
        formData.set('dst_dir', $('#dst-dir').val())
    }
})

dropz.on('addedfile', function (file) {
    $('#upload').removeAttr('disabled');
    $('#upload').bind('click', uploadHandle);
});
uploadHandle = function () {
    dropz.processQueue();//开启文件上传
    $('#upload').unbind('click', uploadHandle);
    $('#upload').attr('disabled', 'disabled');
};
