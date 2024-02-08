#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch movie details.');
  } else {
    try {
      const film = JSON.parse(body);
      const characterUrls = film.characters;

      characterUrls.forEach((url) => {
        request.get(url, (error, response, body) => {
          if (error) {
            console.error(error);
          } else if (response.statusCode !== 200) {
            console.error('Failed to fetch character details.');
          } else {
            try {
              const character = JSON.parse(body);
              console.log(character.name);
            } catch (parseError) {
              console.error(parseError);
            }
          }
        });
      });
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
