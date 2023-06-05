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


// Get the button element
var scrollUpBtn = document.getElementById("scroll-up-btn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollUpBtn.style.display = "block";
  } else {
    scrollUpBtn.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
scrollUpBtn.addEventListener("click", function() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
});