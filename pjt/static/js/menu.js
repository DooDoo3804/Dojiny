function moviesPage() {
  window.location.href = 'http://127.0.0.1:8000/movies/'
}

function behindPage() {
  window.location.href = 'http://127.0.0.1:8000/behinds/'
}

function myPage(userpk) {
  window.location.href = `http://127.0.0.1:8000/mypage/${userpk}/profile/`
}