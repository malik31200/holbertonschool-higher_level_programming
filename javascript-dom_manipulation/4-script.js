const list = document.querySelector('.my_list');
const addli = document.querySelector('#add_item');

addli.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.className = 'my_list';
  newItem.textContent = 'Item';

  list.appendChild(newItem);
});
