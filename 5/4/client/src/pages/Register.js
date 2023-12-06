import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import Button from '../components/Button';
import { Context } from '../index';
import { InputGroup, Control, ErrorLabel } from '../components/Control';
import { NavLink } from 'react-router-dom';

import styles from './Register.module.css';
import { LOGIN_URL, MUSEUM_URL } from "../utils/urls";
import { registration as registerUser } from "../http/userAPI";


const Register= () => {
    const [login, setLogin] = useState("")
    const [password1, setPassword1] = useState("")
    const [password2, setPassword2] = useState("")

    const [loginError, setLoginError] = useState("")
    const [password1Error, setPassword1Error] = useState("")
    const [password2Error, setPassword2Error] = useState("")

    const {userStore} = useContext(Context);

    const navigate = useNavigate();
        
    async function onRegister() {
        var isError = false;

        if (!loginError) {
            if ("" === login) {
                setLoginError("Please enter your login");
                isError = true;
            } else if (login.length < 8) {
                setLoginError("The login must be 8 characters or longer");
                isError = true;
            } else {
                setLoginError("");
            }
        } else {
            isError = true;
        }

        if (!password1Error) {
            if (password1 === "") {
                setPassword1Error("Please enter a password")
                isError = true;
            } else if (password1.length < 8) {
                setPassword1Error("The password must be 8 characters or longer")
                isError = true;
            } else if (password2 === "") {
                setPassword2Error("Please confirm the password")
                isError = true;
            } else if (password1 !== password2) {
                setPassword2Error("The passwords are not the same")
                isError = true;
            } else {
                setPassword1Error("");
                setPassword2Error("");
            }
        } else {
            isError = true;
        }

        if (isError) {
            return;
        }
        
        try {
            const user = await registerUser(login, password1);
            userStore.setUser(user);
            userStore.setIsAuth(true);

            navigate(MUSEUM_URL);
        } catch (errorMessage) {
     //       alert(errorMessage);
            if (typeof errorMessage === 'object' && errorMessage !== null) {
            //    alert("errorMessage");
                if (errorMessage.field === 'password') {
                    setPassword1Error(errorMessage.text)
                } else {
                    setLoginError(errorMessage.text)
                }
            } else {
                setLoginError(errorMessage);
            }
        }
    }

    return (
        <div className={styles.mainContainer}>
            <div className={styles.titleContainer}>
                <div>Register</div>
            </div> 
            <InputGroup>
                <Control
                    value={login}
                    placeholder="Enter your email here"
                    onChange={ev => {setLogin(ev.target.value); setLoginError("");}} 
                />
                <ErrorLabel>{loginError}</ErrorLabel>
            </InputGroup>
            <InputGroup>
                <Control
                    value={password1}
                    type="password"
                    placeholder="Enter your password here"
                    onChange={ev => {setPassword1(ev.target.value); setPassword1Error("");}} 
                />
                <ErrorLabel>{password1Error}</ErrorLabel>
            </InputGroup>
            <InputGroup>
                <Control
                    value={password2}
                    type="password"
                    placeholder="Confirm password"
                    onChange={ev => {setPassword2(ev.target.value); setPassword2Error("");}} 
                />
                <ErrorLabel>{password2Error}</ErrorLabel>
            </InputGroup>
       
            <InputGroup>
                <Button
                    style={{ background: '#F4a0b5' }}
                    onClick={onRegister}
                >
                    Register
                </Button>
            </InputGroup>

            <p>Already registered? <NavLink className={styles.loginLink} to={LOGIN_URL}>Log in</ NavLink></p>
        </div>
    )
}

export default Register