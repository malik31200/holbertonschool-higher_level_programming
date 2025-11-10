document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const hello = document.querySelector('#hello');

  fetch(url).then((response) => {
    return response.json();
  }).then((data) => {
    hello.textContent = data.hello;
  });
});
