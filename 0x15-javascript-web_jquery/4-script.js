/* global $  */
$('#toggle_header').on('click', function () {
  $('header').toggleClass(function () {
    if ($(this).attr('class') === 'green') {
      return 'red';
    } else {
      return 'green';
    }
  });
});
