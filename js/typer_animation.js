var i = 0;
var txt = 'i dont';
var txt2 = ' don\'t know web design'
var speed = 50;

function randint(a, b) {
    var d = b - a;
    return Math.floor(Math.random() * d) * a;
}

function typeWriter() {
    if (i <= txt.length) {
        document.getElementById('typer').innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, randint(30, 50));
    }
    else {
        setTimeout(typeDeleter, 150);
    }
}
function typeDeleter() {
    if (i > 2) {
        txt = txt.slice(0, -1);
        document.getElementById('typer').innerHTML = txt;
        i--;
        setTimeout(typeDeleter, randint(20, 30));
    }
    else {
        setTimeout(typeWriter2, 100);
        i -= 2;
    }
}
function typeWriter2() {
    if (i < txt2.length) {
        document.getElementById('typer').innerHTML += txt2.charAt(i);
        i++;
        setTimeout(typeWriter2, randint(30, 40));
    }
}