// add element, remove element, clear elements
function addElement() {
    // Select direct child of the parent element
    $("UL.my_list").append("<li>item</li>");
}

function removeElement() {
    // Remove individual li elements
    $("UL.my_list li:last-child").remove();
}

function clearList() {
    // Clear all children of UL.my_list
    $("UL.my_list").empty();
}

$(document).ready( () => {
    $("DIV#add_item").on("click", addElement);
    $("DIV#remove_item").on("click", removeElement);
    $("DIV#clear_list").on("click", clearList);
});

