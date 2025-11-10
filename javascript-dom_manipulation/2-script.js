const header = document.querySelector('header');
const clickable = document.querySelector('#red_header');

clickable.addEventListener('click', () => {
  header.classList.add('red');
});
