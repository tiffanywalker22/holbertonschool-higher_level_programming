const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (responsedata) {
  const translatehello = responsedata.hello;
  $('#hello').text(translatehello);
});
