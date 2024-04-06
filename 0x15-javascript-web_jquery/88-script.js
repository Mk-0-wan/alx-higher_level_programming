// fetch the name from the given url and then set it to the div tag

fetch("https://swapi-api.alx-tools.com/api/films/?format=json")
  .then((res) => {
    return res.json();
  })
  .then((data) => {
    const newData = data.results;
    //newData.forEach((item) => {
    //  $("UL#list_movies").append(`<li>${item?.title}</li>`);
    //});
    for (let i = 0; i < data.count; i++) {
      $("UL#list_movies").append(`<li>${newData?.[i]?.title}</li>`);
    }
  })
  .catch((error) => {
    console.log(error);
  });
