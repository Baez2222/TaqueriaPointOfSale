var today = new Date();
var date = today.getFullYear();

var monthDay = today.getDate();
var monthName = today.toLocaleString("default", { month: "long" });
var time = today.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })

document.getElementById("getMonthDay").innerHTML = monthDay;
document.getElementById("getMonth").innerHTML = monthName
document.getElementById("getTime").innerHTML = time;

function addNumber(element) {
    document.getElementById('keypadVar').value = document.getElementById('keypadVar').value + element.value;
}