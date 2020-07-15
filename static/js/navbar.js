const dropdownButton = document.getElementById('dropdown-toggle')
const dropdownMenu = document.getElementById('mobile-dropdown')

dropdownButton.addEventListener('click', toggleDropdown)


function toggleDropdown(){
  if (dropdownMenu.classList.contains('is-active')){
    dropdownMenu.classList.remove('is-active')
  } else {
    dropdownMenu.classList.add('is-active')
  }
}