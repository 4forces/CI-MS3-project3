// Get current date on submit item
function getDate() {
  let dateSubStr = Date().substring(4,15) + ', ' + Date().substring(16,24) ;
  document.getElementById('date').value = dateSubStr;
}
