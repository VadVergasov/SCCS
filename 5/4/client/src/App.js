import './App.css';

import { BrowserRouter } from 'react-router-dom';
import AppRouter from './components/AppRouter';

import Navbar from './components/NavBar';
import { observer } from 'mobx-react-lite';

import { Context } from './index';
import { useContext, useState, useEffect } from 'react';
import { check } from './http/userAPI';



const App = observer(() => {
  const {userStore} = useContext(Context);
  const [loading, setLoading] = useState(true);

  
  useEffect(() => {
    setTimeout(() => {
      check()
        .then(data => {
          userStore.setUser(true);
          userStore.setIsAuth(true);
        })
        .catch(e => console.error(e))
        .finally(() => setLoading(false));
    }, 10)
  },[])

  if (loading) {
    return <p>Loading...</p>
  }

  return (
    <BrowserRouter>
      <Navbar />
      <AppRouter />
    </BrowserRouter>
  );
});

export default App;
