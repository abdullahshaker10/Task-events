updateApi = (url, id, suceessUrl) => {
  fetch(url, {
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    method: "PATCH",
    body: JSON.stringify({ id: id }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      window.location.href = suceessUrl;
    });
};
