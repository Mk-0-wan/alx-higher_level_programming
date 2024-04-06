function getMovieName() {
  fetch("https://swapi-api.alx-tools.com/api/films/?format=json")
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      const newData = data.results;
      newData.forEach((item) => {
        $("UL#list_movies").append(`<li>${item?.title}</li>`);
      });
    })
    .catch((error) => {
      console.log(error);
    });
}

getMovieName();
