window.addEventListener('resize', function() {
  causeRepaintsOn = $("h1, h2, h3, p");

  $(window).resize(function () {
    causeRepaintsOn.css("z-index", 1);
  });
});

