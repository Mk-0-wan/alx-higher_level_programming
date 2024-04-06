// Adding a toggle class function
$(".green").on("click", function() {
  if ($(this).hasClass("green")) {
    $(this).removeClass("green");
    $(this).addClass("red");
  }
  else if ($(this).hasClass("red")) {
    $(this).removeClass("red");
    $(this).addClass("green");
  }
});
