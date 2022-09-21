// using https://stefanbohacek.com/hellosalut/?lang=fr instead of https://fourtonfish.com/hellosalut/?lang=fr
// because https://fourtonfish.com/hellosalut/?lang=fr is redirected.
$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data, textStatus) {
  if (textStatus === 'success') {
    $('DIV#hello').text(data.hello);
  }
});
