// add element, remove element, clear elements
function addElement(){
  // look how to select the direct child of the parent element
  $("UL.my_list li").after("<li>item</li>");
}

function removeElement() {
  $("UL.my_list li").remove();
}

function clear() {
  $("UL.my_list").remove();
}

$("DIV#add_item").on("click", addElement);
$("DIV#remove_item").on("click", removeElement);
$("DIV#clear_list").on("click", clear);
