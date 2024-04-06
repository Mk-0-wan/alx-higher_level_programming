// get the property name of the given object and add it to the div tag
fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    const dictObject = data;

    for (propName in dictObject) {
      if (propName === "hello") {
        $("DIV#hello").text(`${dictObject[propName]}`);
      }
    }
  })
  .catch((error) => {
    console.log(error);
  })
