import {makeAutoObservable} from 'mobx';


export default class UserStore {
    constructor() {
        this._isAuth = false;
        this._user = {};

        this._users = [];
        this._roles = [];

        makeAutoObservable(this);
    }

    setIsAuth(bool) {
        this._isAuth = bool;
    }

    setUser(user) {
        this._user = user;
    }

    setRoles(roles) {
        this._roles = roles;
    }

    setUsers(users) {
        this._users = users;
    }

    get isAuth() {
        return this._isAuth;
    }

    get user() {
        return this._user;
    }

    get roles() {
        return this._roles;
    }

    get users() {
        return this._users;
    }

}