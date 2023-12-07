import React, { useContext } from 'react';
import { Context } from '../index';
import { NavLink } from 'react-router-dom';

import { observer } from 'mobx-react-lite';

import { useState } from 'react'
import styles from './NavBar.module.css';
import Clock from './Clock';
import BitcoinRate from './BitcoinRate';
import JokeOfTheDay from './JokeOfTheDay';

import { MUSEUM_URL, LOGIN_URL, ADMIN_URL, REGISTRATION_URL, ABOUT_URL } from '../utils/urls';


const Navbar = observer(() => {
  const [isActive, setIsActive] = useState(false);
  const [isAuth, setIsAuth] = useState(false);
  const {userStore} = useContext(Context);

  const toggleActiveClass = () => {
    setIsActive(!isActive);
  };

  const removeActive = () => {
    setIsActive(false)
  }

  const logOut = () => {
    userStore.setUser(null);
    userStore.setIsAuth(false);
  }


  return (
    <header>
      <nav className={styles.navbar}>
        <NavLink to={MUSEUM_URL} className={`${styles.logo} ${styles.navLink}`}>Museum</NavLink>

        <ul className={`${styles.navMenu} ${isActive ? styles.active : ''}`}>
          <li onClick={removeActive}>
            <NavLink className={styles.navLink} to={MUSEUM_URL}>Home</NavLink>
          </li>
          {userStore.isAuth
            ? <>
                {userStore.user.roleId == 1 &&
                  <li onClick={removeActive}>
                    <NavLink className={styles.navLink} to={ADMIN_URL}>Admin</NavLink>
                  </li>
                }
                <li onClick={removeActive}>
                  <NavLink className={styles.navLink} to={ABOUT_URL}>About</NavLink>
                </li>
                <li onClick={removeActive}>
                  <NavLink className={styles.navLink} to={MUSEUM_URL} onClick={logOut}>Logout</NavLink>
                </li>
                <li>
                  <Clock />
                </li>
                <li>
                  <BitcoinRate />
                </li>
                <li>
                  <JokeOfTheDay />
                </li>
              </> 
            : <>
                <li onClick={removeActive}>
                  <NavLink className={styles.navLink} to={ABOUT_URL}>About</NavLink>
                </li>
                <li onClick={removeActive}>
                  <NavLink className={styles.navLink} to={REGISTRATION_URL}>Register</NavLink>
                </li>
                <li onClick={removeActive}>
                  <NavLink className={styles.navLink} to={LOGIN_URL}>Login</NavLink>
                </li>
                <li>
                  <Clock />
                </li>
                <li>
                  <BitcoinRate />
                </li>
                <li>
                  <JokeOfTheDay />
                </li>
              </>
          }
        </ul>

        <div className={`${styles.hamburger} ${isActive ? styles.active : ''}`}  onClick={toggleActiveClass}>
          <span className={styles.bar}></span>
          <span className={styles.bar}></span>
          <span className={styles.bar}></span>
        </div>
      </nav>
    </header>
  );
});


export default Navbar;
