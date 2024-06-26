// const form = document.querySelector('form');
// const submitURL = form.getAttribute('action');
// let fileInput = document.querySelector('input[type="file"]');
// console.log('activated.');
// form.addEventListener('submit', (e)=>{
//     e.preventDefault();
//     const formData = new FormData();
//     formData.append('file', fileInput.files[0]);
//     fetch(submitURL,{
//         method:"PATCH",
//         body: formData,
//     })
//     .then(response => response.json())
//     .then(data => console.log(data))
// });