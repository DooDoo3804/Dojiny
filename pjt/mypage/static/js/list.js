
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
const star5form = document.querySelector('#star5-form')
const star4form = document.querySelector('#star4-form')
const star3form = document.querySelector('#star3-form')
const star2form = document.querySelector('#star2-form')
const star1form = document.querySelector('#star1-form')

var fiveList = 0
var fourList = 0
var threeList = 0
var twoList = 0
var oneList = 0

formArr = [star5form, star4form, star3form, star2form, star1form]

formArr.forEach(form => {
  if (form != null) {

  }
});

  console.log('not null')
  star5form.addEventListener('subimt', event => {
    event.preventDefault()
    const userId = event.target.dataset.userId
    var stars = event.target.dataset.stars
    console.log(event.submitter.value)
    if (event.submitter.value === 'next'){
      fiveList += 1
    }
    else {
      if (fiveList !== 0) {
        fiveList -= 1
      }
    }

    content_data = {
      'stars': stars,
      'fiveList': fiveList,
    }

    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/mypage/${userId}/likemovies/`,
      headers: {'X-CSRFToken': csrftoken},
      data: JSON.stringify(content_data),
    })
    .then((res) => {
      console.log(res)
    })
    .catch((res) => {
      console.log(res)
    })
  })

// nextArr.forEach(next => {
//   if (next != null) {
//     next.addEventListener('click', event => {
//       // img5stars.innerHTML = ``
//       const userId =event.target.dataset.movieStars
//       event.preventDefault()
//       pageCount += 1
//       var content_data = {
//         'pageCount': pageCount,
//       }
//       axios({
//         method: 'post',
//         url: `http://127.0.0.1:8000/mepage/${userId}/likemovies/`,
//         headers: {'X-CSRFToken': csrftoken},
//         data: JSON.stringify(content_data),
//       })
//       .then((res) => {
//         console.log(res)  
//         movies = res.data
//         console.log(typeof(movies))
//         for (let i=0; i<20; i++) {
//           movie = movies[i]
//           movieList.innerHTML += `
//           <a href="{% url 'movies:detail' movie.pk %}">
//             <img src="https://image.tmdb.org/t/p/w500${movie.poster_url}" alt="movie img" class="movie-img">
//             <div class="info">${movie.title}</div>
//           </a>
//           `
//         }
//     })})}})
  

  // 비동기로 데이터 받아오기
  