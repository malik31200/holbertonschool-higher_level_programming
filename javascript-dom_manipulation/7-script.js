const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listmovies = document.querySelector('#list_movies');

fetch(url).then((response) => {
  return response.json();
}).then((data) => {
  data.results.forEach(film => {
    const li = document.createElement('li');
    li.textContent = film.title;
    listmovies.appendChild(li);
  });
});
