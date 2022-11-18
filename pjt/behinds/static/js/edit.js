const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
// 수정 폼 불러오기 토글

const updateBtns = document.querySelectorAll(`.update-form`)
updateBtns.forEach(updateBtn => {
  updateBtn.addEventListener('submit', function (event) {
    event.preventDefault()
    const commentContent = event.target.dataset.commentContent
    const commentId = event.target.dataset.commentId
    const targetTextDiv = document.querySelector(`#edit-div${commentId}`)
    const targetTextArea = document.querySelector(`#edit-area${commentId}`)
    const updateBtnAxios = document.querySelector(`.update-form-axios${commentId}`)
    targetTextDiv.setAttribute('style','display:block;')
    targetTextArea.value = commentContent
    updateBtn.setAttribute('style','display:none;')
    updateBtnAxios.setAttribute('style','display:block;')
  })
})

const updateBtnAxioses = document.querySelectorAll(`.udpate-form-axios`)
updateBtnAxioses.forEach(updateBtnAxios => {
  updateBtnAxios.addEventListener('submit', function (event) {
    event.preventDefault()
    const behindId = event.target.dataset.behindId
    const commentId = event.target.dataset.commentId
    const targetTextArea = document.querySelector(`#edit-area${commentId}`)
    const updateBtn = document.querySelector(`.update-form${commentId}`)
    var content_data = {
      'behindId': behindId,
      'content': targetTextArea.value,
      'commentId': commentId,
      'csrftoken': csrftoken,
    }
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/behinds/${behindId}/comment_update/${commentId}/`,
      headers: {'X-CSRFToken': csrftoken},
      data: JSON.stringify(content_data),
    })
    .then(response => {댓글
      // const commentContent = event.target.dataset.commentContent
      const targetTextDiv = document.querySelector(`#edit-div${commentId}`)
      const targetTextArea = document.querySelector(`#edit-area${commentId}`)
      targetTextArea.value = ''
      const updateBtnAxios = document.querySelector(`.update-form-axios${commentId}`)
      targetTextDiv.setAttribute('style','display:none;')
      updateBtn.setAttribute('style','display:block;')
      updateBtnAxios.setAttribute('style','display:none;')

      const data = response.data
      const commentTag = document.querySelector(`#comment-${ commentId }`)
      commentTag.innerText = data.editedContent

    })
    .catch(error => {
      console.log(error)
    })
  })
})