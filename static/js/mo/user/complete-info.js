function confirm() {
    let username= $('#username').val();
    let wechat= $('#wechat').val();
    let phone= $('#phone').val();
    let avatar= $('#avatar').val();
    let jobtitle= $('#jobtitle').val();
    let role= $('#role').val();
    if(!username){
        swal('Info Error', 'Username is empty.', 'error');
    }
    if(!wechat){
        swal('Info Error', 'Wechat is empty.', 'error');
    }
    if(!phone){
        swal('Info Error', 'Phone is empty.', 'error');
    }
    if(!avatar){
        swal('Info Error', 'Avatar is empty.', 'error');
    }
    if(!jobtitle){
        swal('Info Error', 'Jobtitle is empty.', 'error');
    }
    if(!role){
        swal('Info Error', 'Role is empty.', 'error');
    }
    $.ajax({
        url: apiUrl.users.
    })
}