// Upload photo
// document.querySelector('.custom-file-input').addEventListener('change',function(e){
//   var fileName = document.getElementById("myInput").files[0].name;
//   var nextSibling = e.target.nextElementSibling
//   nextSibling.innerText = fileName
// })

// Get current date
function getDate() {
  let dateSubStr = Date().substring(4,15)
  document.getElementById('date').value = dateSubStr;
}

function changeX() {
    document.getElementById('delete').innerHTML = '<i id="fa-cross" class="fa fa-remove"></i>';
}

function changeDelete() {
    document.getElementById('fa-cross').innerHTML = '<span id="delete">Delete</span>';
}

function changePencil() {
    document.getElementById('edit').innerHTML = '<i id="fa-pencil" class="fa fa-pencil"></i>';
}

function changeEdit() {
    document.getElementById('fa-pencil').innerHTML = '<span id="edit">Edit</span>';
}