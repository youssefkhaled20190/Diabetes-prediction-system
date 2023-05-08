const toggleBtn=document.querySelector('.toggle_btn');
const toggleBtnIcon=document.querySelector('.toggle_btn i');
const dropDownMenu=document.querySelector('.dropdown_menu');
toggleBtn.onclick=function(){
  dropDownMenu.classList.toggle('open');
  const isOpen=dropDownMenu.classList.contains('open')

  toggleBtnIcon.classList=isOpen
  ?'fa-solid fa-xmark'
  :'fa-solid fa-bars fa-sm'
}

function closeNavbarMenu(event) {
  if (!dropDownMenu.contains(event.target) && !toggleBtn.contains(event.target) && dropDownMenu.classList.contains('open')) {
    dropDownMenu.classList.remove('open');
    toggleBtnIcon.classList = 'fa-solid fa-bars fa-sm';
    // set class to bar icon if menu is closed
  }
}

window.addEventListener('click', closeNavbarMenu);