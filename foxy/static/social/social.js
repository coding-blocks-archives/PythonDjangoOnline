function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function likePost(postId) {
  return fetch('/post/' + postId + '/like', {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    }
  }).then(() => {
    window.location.reload()
  })
}

function commentPost(postId, comment) {
  const formData = new FormData()
  formData.append('content', comment)
  return fetch('/post/' + postId + '/comment', {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    },
    body: formData,
  }).then(() => {
    window.location.reload()
  })
}
