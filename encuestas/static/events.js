let toggle = document.querySelector('.toggle');
let navigation = document.querySelector('.navigation');
let main = document.querySelector('.main');

toggle.onclick = function(){
    navigation.classList.toggle('active');
    main.classList.toggle('active');
}
//add hovered class 
// let 
let list = document.querySelectorAll('.navigation li');
function activeLink(){
    console.log("Hola")
    list.forEach((item) =>
    item.classList.remove('hovered'));
    this.classList.add('hovered');
}

list.forEach((item)=>{
    item.addEventListener('mouseover',activeLink);
    item.addEventListener('click',activeLink);
});