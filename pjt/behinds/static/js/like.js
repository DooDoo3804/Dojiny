
const forms = document.querySelectorAll('.like-img-button')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

forms.forEach(form => {
  form.addEventListener('click', function (event) {
    event.preventDefault()
    // console.log(event)
    const behindId = event.target.dataset.behindId
    console.log(1)
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/behinds/${behindId}/likes/`,
      headers: {'X-CSRFToken': csrftoken},
    })
      .then(response => {
        console.log(response)
      })
      .catch(err => {
        console.log(err)
      })
    })
  })
  // const isFollowed = response.data.isFollowed
  // if (isFollowed === true) {
  //   followBtn.innerText = '언팔로우'
  // } else {
  //   followBtn.innerText = '팔로우'
  // }