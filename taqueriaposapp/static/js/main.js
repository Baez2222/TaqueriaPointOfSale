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

function changeTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    for (i=0; i < document.getElementsByClassName(tabName).length; i++){
      document.getElementsByClassName(tabName)[i].style.display = "block";
      evt.currentTarget.className += " active";
    }
}