var today = new Date();
var date = today.getFullYear();

var monthDay = today.getDate();
var monthName = today.toLocaleString("default", { month: "long" });

document.getElementById("getMonthDay").innerHTML = monthDay;
document.getElementById("getMonth").innerHTML = monthName


function addNumber(element) {
    document.getElementById('keypadVar').value = document.getElementById('keypadVar').value + element.value;
}