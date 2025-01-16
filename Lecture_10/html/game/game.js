document.addEventListener('DOMContentLoaded', ()=>{
    var canvas = document.getElementById('gameCanvas');
    var context = canvas.getContext('2d');


    var paddle= {
        width:100,
        height:10,
        x: canvas.width / 2-50,
        y: canvas.height -20
    };

    function drawPadddle(){
        context.fillStyle='blue';
        context.fillRect(paddle.x, paddle.y, paddle.width. paddle.height);
    }

    var ball={
        radius:10,
        x:Math.random()*(canvas.width-20)
    }
});