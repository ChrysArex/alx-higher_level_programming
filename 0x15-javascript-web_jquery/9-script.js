/* global $  */
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data, state) {
  $('#hello').text(data.hello);
});
