// fetch the name from the given url and then set it to the div tag
//
console.log("Thenameistheprimeagenlostapprentice");
// const URL = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
async function getName() {
  const URL =  await fetch("https://swapi-api.alx-tools.com/api/films/?format=json");
  const resp = await URL.json();
  //console.log(resp);
  $("DIV#character").text(resp.name);
}
getName();
