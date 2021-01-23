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

// side menu script
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

// toggle dropdown menu on cart item
/* When the user clicks on the button,
  toggle between hiding and showing the dropdown content */
function myFunction(cartItem_ID) {
document.getElementById(cartItem_ID).classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
    var openDropdown = dropdowns[i];
    if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
    }
    }
}
}
// only have one dropdown menu open at a time
function toggleExtraPopups(ID){
var dropdowns = document.getElementsByClassName("dropdown-content");
var i;
for ( i = 0; i < dropdowns.length; i++){
    var openDropdown = dropdowns[i];
    if (openDropdown.classList.contains('show') && openDropdown.id != ID){
    openDropdown.classList.remove('show');
    }
}
}