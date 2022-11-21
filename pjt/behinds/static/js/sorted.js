const selectedTypes = document.querySelector("#types")
const popularForm = document.querySelector("#popular-form")
const cerentForm = document.querySelector("#recent-form")

selectedTypes.addEventListener('change', event => {
  var selected = event.target.value
  if (selected === 'popular') {
    console.log('popular')
    popularForm.classList.remove('not-visible')
    cerentForm.classList.add('not-visible')
  }
  else {
    popularForm.classList.add('not-visible')
    cerentForm.classList.remove('not-visible')
  }
})