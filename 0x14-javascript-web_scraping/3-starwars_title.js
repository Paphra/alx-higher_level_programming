#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch movie.');
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
