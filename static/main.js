// Upload photo
// document.querySelector('.custom-file-input').addEventListener('change',function(e){
//   var fileName = document.getElementById("myInput").files[0].name;
//   var nextSibling = e.target.nextElementSibling
//   nextSibling.innerText = fileName
// })




// $(function() {
//     toastr.options = {
//     "debug": false,
//     "positionClass": "toast-bottom-full-width",
//     "onclick": null,
//     "fadeIn": 300,
//     "fadeOut": 1000,
//     "timeOut": 5000,
//     "extendedTimeOut": 1000
//     }
// })

// Get current date
function getDate() {
  let dateSubStr = Date().substring(0,3) + 'day, '+ Date().substring(4,15) + ', ' + Date().substring(16,24) ;
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