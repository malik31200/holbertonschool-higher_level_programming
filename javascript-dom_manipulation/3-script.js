const header = document.querySelector('header');
const clickable = document.querySelector('#toggle_header');

clickable.addEventListener('click', () => {
  if (header.style.color === 'red') {
    header.style.color = 'green';
  } else {
    header.style.color = 'red';
  }
});
