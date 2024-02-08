#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch movies.');
  } else {
    try {
      const films = JSON.parse(body).results;
      let count = 0;
      films.forEach((film) => {
        if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
        }
      });
      console.log(count);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
