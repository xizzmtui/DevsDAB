const cont = document.querySelector('.cont');
const seats = document.querySelectorAll('.ro .seat:not(.occupied)');

cont.addEventListener('click', (e) => {
  if(e.target.classList.contains('seat') && !e.target.classList.contains('occupied')){
    e.target.classList.toggle('selected');
  }
})
