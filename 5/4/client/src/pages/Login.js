import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import Button from '../components/Button';
import { Context } from '../index';
import { InputGroup, Control, ErrorLabel } from '../components/Control';
import { NavLink } from 'react-router-dom';

import styles from './Login.module.css';
import { REGISTRATION_URL, MUSEUM_URL } from "../utils/urls";
import { login as loginUser } from "../http/userAPI";


// import Button2 from '../components/Button2';


function Login() {
    const [login, setLogin] = useState("")
    const [password, setPassword] = useState("")

    const [loginError, setLoginError] = useState("")
    const [passwordError, setPasswordError] = useState("")

    const {userStore} = useContext(Context);
    
    const navigate = useNavigate();
        
    async function onLogin() {
        var isError = false;

        if (!loginError) {
            if (login === "") {
                setLoginError("Please enter your login")
                isError = true;
            } else if (login.length < 8) {
                setLoginError("Invalid login")
                isError = true;
            } else {
                setLoginError("")
            }
        } else {
            isError = true;
        }

        if (!passwordError) {
            if (password === "") {
                setPasswordError("Please enter a password")
                isError = true;
            } else if (password.length < 8) {
                setPasswordError("Invalid password")
                isError = true;
            } else {
                setPasswordError("")
            }
        } else {
            isError = true;
        }

        if (isError) {
            return;
        }
        
        try {
            const user = await loginUser(login, password); 
            userStore.setUser(user);
            userStore.setIsAuth(true);

            navigate(MUSEUM_URL);
        } catch (errorMessage) {
            if (typeof errorMessage === 'object' && errorMessage !== null) {
                if (errorMessage.field === 'password') {
                    setPasswordError(errorMessage.text)
                } else {
                    setLoginError(errorMessage.text)
                }
            } else {
                setLoginError(JSON.stringify(errorMessage));
            }
        }
    }

    return (
        <div className={styles.mainContainer}>
            <div className={styles.titleContainer}>
                <div>Login</div>
            </div> 
            <InputGroup>
                <Control
                    value={login}
                    placeholder="Enter your email"
                    onChange={ev => {setLogin(ev.target.value); setLoginError("");}} 
                />
                <ErrorLabel>{loginError}</ErrorLabel>
            </InputGroup>
            <InputGroup>
                <Control
                    value={password}
                    type="password"
                    placeholder="Enter your password"
                    onChange={ev => {setPassword(ev.target.value); setPasswordError("");}} 
                />
                <ErrorLabel>{passwordError}</ErrorLabel>
            </InputGroup>
       
            <InputGroup>
                <Button
                    style={{ background: '#F4a0b5' }}
                    onClick={ev => onLogin()}
                >
                    Log in
                </Button>
            </InputGroup>

            <p>Not registered? <NavLink className={styles.registerLink} to={REGISTRATION_URL}>Register</ NavLink></p>
        </div>
    )
}

export default Login