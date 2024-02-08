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

      function getChar (index) {
        if (index < characterUrls.length) {
          request.get(characterUrls[index], (error, response, body) => {
            if (error) {
              console.error(error);
              getChar(index + 1);
            } else if (response.statusCode !== 200) {
              console.error('Failed to fetch character details.');
              getChar(index + 1);
            } else {
              try {
                const character = JSON.parse(body);
                console.log(character.name);
                getChar(index + 1);
              } catch (parseError) {
                console.error(parseError);
                getChar(index + 1);
              }
            }
          });
        }
      }
      getChar(0);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
