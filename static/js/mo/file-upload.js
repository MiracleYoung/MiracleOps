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


// Get the template HTML and remove it from the doument
// var previewNode = document.querySelector("#template");
// previewNode.id = "";
// var previewTemplate = previewNode.parentNode.innerHTML;
// previewNode.parentNode.removeChild(previewNode);
//
// var myDropzone = new Dropzone(document.body, { // Make the whole body a dropzone
//     url: '/api/deploy/file-upload/',
//     // uploadMultiple: true,
//     parallelUploads: 5,
//     autoProcessQueue: false,
//     // sendingmultiple: function (file, xhr, formData) {
//     //     formData.set('glob', $('#reg').val())
//     //     formData.set('dst_dir', $('#dst-dir').val())
//     // },
//     thumbnailWidth: 80,
//     thumbnailHeight: 80,
//     previewTemplate: previewTemplate,
//     autoQueue: false, // Make sure the files aren't queued until manually added
//     previewsContainer: "#previews", // Define the container to display the previews
//     clickable: ".fileinput-button" // Define the element that should be used as click trigger to select files.
// });
//
// uploadHandle = function () {
//     myDropzone.processQueue();// start upload file
// };
//
// myDropzone.on("addedfile", function (file) {
//     // Hookup the start button
//     // $('.submit').bind('click', uploadHandle);
//     file.previewElement.querySelector(".start").onclick = function () {
//         myDropzone.enqueueFile(file);
//     };
// });
//
// // Update the total progress bar
// myDropzone.on("totaluploadprogress", function (progress) {
//     document.querySelector("#total-progress .progress-bar").style.width = progress + "%";
// });
//
// myDropzone.on("sending", function (file) {
//     // Show the total progress bar when upload starts
//     document.querySelector("#total-progress").style.opacity = "1";
//     // And disable the start button
//     file.previewElement.querySelector(".start").setAttribute("disabled", "disabled");
// });
//
// // Hide the total progress bar when nothing's uploading anymore
// myDropzone.on("queuecomplete", function (progress) {
//     document.querySelector("#total-progress").style.opacity = "0";
// });
//
// // Setup the buttons for all transfers
// // The "add files" button doesn't need to be setup because the config
// // `clickable` has already been specified.
// document.querySelector("#actions .start").onclick = function () {
//     myDropzone.enqueueFiles(myDropzone.getFilesWithStatus(Dropzone.ADDED));
// };
// document.querySelector("#actions .cancel").onclick = function () {
//     myDropzone.removeAllFiles(true);
// };


// Now fake the file upload, since GitHub does not handle file uploads
// and returns a 404
//
// var minSteps = 6,
//     maxSteps = 60,
//     timeBetweenSteps = 100,
//     bytesPerStep = 100000;
//
// myDropzone.uploadFiles = function (files) {
//     var self = this;
//
//     for (var i = 0; i < files.length; i++) {
//
//         var file = files[i];
//         totalSteps = Math.round(Math.min(maxSteps, Math.max(minSteps, file.size / bytesPerStep)));
//
//         for (var step = 0; step < totalSteps; step++) {
//             var duration = timeBetweenSteps * (step + 1);
//             setTimeout(function (file, totalSteps, step) {
//                 return function () {
//                     file.upload = {
//                         progress: 100 * (step + 1) / totalSteps,
//                         total: file.size,
//                         bytesSent: (step + 1) * file.size / totalSteps
//                     };
//
//                     self.emit('uploadprogress', file, file.upload.progress, file.upload.bytesSent);
//                     if (file.upload.progress == 100) {
//                         file.status = Dropzone.SUCCESS;
//                         self.emit("success", file, 'success', null);
//                         self.emit("complete", file);
//                         self.processQueue();
//                     }
//                 };
//             }(file, totalSteps, step), duration);
//         }
//     }
// }