import React, { useState, useEffect } from 'react';
import axios from 'axios';

const JokeOfTheDay = () => {
  const [joke, setJoke] = useState(null);

  useEffect(() => {
    const fetchJoke = async () => {
      try {
        const response = await axios.get(
          'https://v2.jokeapi.dev/joke/Any?type=single'
        );
        setJoke(response.data.joke);
      } catch (error) {
        console.error('Error fetching joke:', error);
      }
    };

    fetchJoke();

    const intervalId = setInterval(fetchJoke, 24 * 60 * 60 * 1000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return (
    <div style={{color: 'rgba(255, 255, 255, 0.55)'}}>
      <h2>Joke of the Day</h2>
      {joke !== null ? (
        <p>{joke}</p>
      ) : (
        <p>Loading joke...</p>
      )}
    </div>
  );
};

export default JokeOfTheDay;
