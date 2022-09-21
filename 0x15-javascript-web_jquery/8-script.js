$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
  if (textStatus === 'success') {
    const allFilms = data.results;
    for (const film of allFilms) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    }
  }
});
