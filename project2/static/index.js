document.addEventListener('DOMContentLoaded', ()=> {
    //connect to socket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    
    //configure send button
    socket.on('connect',()=>{
        
        //button emits a "send message" event
        document.querySelector('#send').onclick = ()=> {
            var message = document.querySelector('#message').value;
            var name = document.querySelector('#name').value;
            socket.emit('send message',{'message':message,'name':name});
        };
        
    });
    
    //When a new message is sent, add it to the list
    socket.on('recive messege',data=>{
        var ch = document.createElement('ch');
        var li = document.createElement('li');
        li.innerHTML = `${data.name}:${data.message}:{data.ch}`;
        document.querySelector('#messages').append(li);
    });
});

