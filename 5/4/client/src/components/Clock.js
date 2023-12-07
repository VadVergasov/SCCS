import React, { useState, useEffect } from 'react';
import moment from 'moment-timezone';

const Clock = () => {
  const [currentTime, setCurrentTime] = useState(moment());

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentTime(moment());
    }, 1000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  const userTimeZone = moment.tz.guess();

  return (
    <div style={{color: 'rgba(255, 255, 255, 0.55)'}}>
      <p>Current Time: {currentTime.format('HH:mm:ss')}</p>
      <p>Time Zone: {userTimeZone}</p>
    </div>
  );
};

export default Clock;
