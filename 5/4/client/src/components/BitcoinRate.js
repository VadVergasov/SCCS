import React, { useState, useEffect } from 'react';
import axios from 'axios';

const BitcoinRate = () => {
  const [bitcoinRate, setBitcoinRate] = useState(null);

  useEffect(() => {
    const fetchBitcoinRate = async () => {
      try {
        const response = await axios.get(
          'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
        );
        setBitcoinRate(response.data.bitcoin.usd);
      } catch (error) {
        console.error('Error fetching Bitcoin rate:', error);
      }
    };
    fetchBitcoinRate();
    const intervalId = setInterval(fetchBitcoinRate, 60000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return (
    <div style={{color: 'rgba(255, 255, 255, 0.55)'}}>
      <h2>Bitcoin Rate</h2>
      {bitcoinRate !== null ? (
        <p>Current Rate: ${bitcoinRate}</p>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default BitcoinRate;
