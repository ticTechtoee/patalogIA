 //Show Image before uploading
        function uploadImage(input) {
            if (input.files && input.files[0]) {
                var url = URL.createObjectURL(input.files[0]);
                $('#canvas').attr('style', 'background-image:url(' + url + ')');
            }
        }
        document.getElementById("id_questionImage").onchange = function () { uploadImage(this) };
        // Creating the demarcation tool

    function getCursorPosition(canvas, event) {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    return { x, y };
}

//Canvas
var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
//Variables
var canvasx = $(canvas).offset().left;
var canvasy = $(canvas).offset().top;
var last_mousex = last_mousey = 0;
var mousex = mousey = 0;
var mousedown = false;

//Mousedown
$(canvas).on('mousedown', function(e) {
    var pos = getCursorPosition(canvas, e);
    last_mousex = pos.x;
    last_mousey = pos.y;
    mousedown = true;
    x1 = e.clientX;
    y1 = e.clientY;
});

//Mousemove
$(canvas).on('mousemove', function(e) {
    var pos = getCursorPosition(canvas, e);
    mousex = pos.x;
    mousey = pos.y;
    if(mousedown) {
        ctx.clearRect(0,0,canvas.width,canvas.height); //clear canvas
        ctx.beginPath();
        var width = mousex-last_mousex;
        var height = mousey-last_mousey;
        ctx.rect(last_mousex,last_mousey,width,height);
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 2;
        ctx.stroke();
    }
    //Output
    x2 = e.clientX;
    y2 = e.clientY;
});


//Mouseup
$(canvas).on('mouseup', function(e) {
    mousedown = false;
     //for testing
     document.getElementById("x1").value = x1;
    document.getElementById("y1").value = y1;
    document.getElementById("x2").value = x2;
    document.getElementById("y2").value = y2;
});