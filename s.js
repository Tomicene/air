const tapElement = document.getElementById("tap_area");
const tap = tapElement ? tapElement.value : "";

let balance = localStorage.getItem("balance") !== null ? parseFloat(localStorage.getItem("balance")) : 0;
function incr1() {
    balance += 0.5;
    localStorage.setItem("balance", balance);
    // const scr = localStorage.getItem("balance");
    // document.getElementById("score").innerHTML = scr;


}
function ott(){
    document.getElementById("taskbb").style.display= "block";
    document.getElementById("taskaa").style.display= "none";
}
function tlt(){
    document.getElementById("taskaa").style.display= "block";
    document.getElementById("taskbb").style.display= "none";
}
function load(){
    let cor = localStorage.getItem("balance")
    let cor3 = localStorage.getItem("balance")
    let cor2 = localStorage.getItem("balance")
    let cor1 = localStorage.getItem("balance")
    document.getElementById("score").innerHTML = cor;
    document.getElementById("score1").innerHTML = cor1;
    document.getElementById("score2").innerHTML = cor2;
    document.getElementById("score3").innerHTML = cor3;
}
setInterval(load, 1 );
function tasks(){
    document.getElementById("home").style.display= "none";
    document.getElementById("busniess").style.display= "none";
    document.getElementById("referals").style.display= "none";
    document.getElementById("earnings").style.display= "none";
    document.getElementById("tasks").style.display= "block";

}
function home(){
    document.getElementById("home").style.display= "block";
    document.getElementById("busniess").style.display= "none";
    document.getElementById("referals").style.display= "none";
    document.getElementById("earnings").style.display= "none";
    document.getElementById("tasks").style.display= "none";

}

function busn(){
    document.getElementById("home").style.display= "none";
    document.getElementById("busniess").style.display= "block";
    document.getElementById("referals").style.display= "none";
    document.getElementById("earnings").style.display= "none";
    document.getElementById("tasks").style.display= "none";

}