var socket = new WebSocket('ws://localhost:3368');
socket.onmessage = function (result, nTime) {
    alert("从服务端收到的数据:");
    alert("近期一次发送数据到如今接收一共使用时间:" + nTime);
    console.log(result);
}