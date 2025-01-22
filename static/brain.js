
document.addEventListener('keydown', function(e) {
    
    if (e.ctrlKey && (e.key === '=' || e.key === '-' || e.key === '+')) {
        e.preventDefault();  
    }
});

document.addEventListener('wheel', function(e) {
    if (e.ctrlKey) {
        e.preventDefault();  
    }
}, { passive: false });
var2 = false;
var3 = false;
button = document.getElementById("2");
button.addEventListener("click" , function(event){
if(var2 == true && var3 == true){
document.getElementById("1").submit();
}
event.preventDefault();
})

function move(event , nextinput , id , id2){
const mail = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;
const passw = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;\"'<>,.?/\\|`~]).{8,}$/;
 var f = mail.test(document.getElementById('inp2').value);
 var f2 = passw.test(document.getElementById('inp3').value);
 var f3 = document.getElementById("inp1").value
 var inps = document.getElementById(id)
if(f === true || id === "inp1"){
if(event.key === "Enter"){
    event.preventDefault();
    document.getElementById(nextinput).focus();}}
if(event.key === "Enter"){
event.preventDefault();
}
if( f2 === true && event.key === "Enter" && f3 != "" && f === true ){
document.getElementById("1").submit();
}
if(f === false ){
    var2 = false
}
if(f2 === false ){
    var3 = false
}
if(inps != '' && id === 'inp1'){
    document.getElementById(id2).style.display = 'none';
}
if(f === true && id === 'inp2'){
    var2=true
    document.getElementById(id2).style.display = 'none';
}
if(f === false && id === 'inp2'){
    document.getElementById(id2).style.display = 'grid';
}
if(f2 === true && id === 'inp3'){
    var3=true
    document.getElementById(id2).style.display = 'none';}
if(f2 === false && id === 'inp3'){
    document.getElementById(id2).style.display = 'grid';
}    
}
function focout(id){
    document.getElementById(id).style.display = 'none';
    var form = document.getElementById('1').clientHeight
    var body = document.getElementById('8').clientHeight
    document.getElementById('1').style.height = ((form/ body) * 100) - 10 + "%";
    
  }
function focin(id , id2){
  document.getElementById(id).style.display = 'grid';
  var form = document.getElementById('1').clientHeight;
  var body = document.getElementById('8').clientHeight;
  document.getElementById('1').style.height = ((form/ body) * 100) + 10 + "%";
  
  if(id2==='inp1'&& document.getElementById(id2).value != ''){
    document.getElementById(id).style.display = 'none';
  }
  if(id2==='inp2'&& var2 === true){
    document.getElementById(id).style.display = 'none';
  }
  if(id2==='inp3'&& var3 === true){
    document.getElementById(id).style.display = 'none';
  }
}
