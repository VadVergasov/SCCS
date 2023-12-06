import { $host, $authHost } from './index';
import { jwtDecode } from 'jwt-decode';


export const registration = async (login, password) => {
    try {
        const {data} = await $host.post('api/user/registration', {login, password});
        localStorage.setItem('token', data.token)
        return jwtDecode(data.token);
    } catch (e) {
       
        let fieldError;

        try {
            fieldError = JSON.parse(e?.response?.data?.message)
        } catch (jsonError) {
            throw (e?.response?.data?.message.split(':')[1] || "Incorrect format");
        }

        throw fieldError;
    }
}

export const login = async (login, password) => {
    try {
        const {data} = await $host.post('api/user/login', {login, password});
        localStorage.setItem('token', data.token)

        return jwtDecode(data.token);
    } catch (e) {
        throw (JSON.parse(e?.response?.data?.message) || "Unexpected error");
    }
}

export const check = async () => {
    const {data} = await $authHost.get('api/user/auth');

    localStorage.setItem('token', data.token)
    return jwtDecode(data.token);
}

export const getUsers = async (roleId) => {
    const res = await $host.get('api/user', { params: {roleId}});

    const {data} = res;
    return data;
}


export const updateUser = async (id, user) => {
    const {data} = await $authHost.patch(`api/user/${id}`, user);
    return data;
}






export const createRole = async (name) => {
    const {data} = await $authHost.post('api/role', {name});
    return data;
}

export const getRoles = async () => {
    const {data} = await $host.get('api/role');
    return data;
}

export const updateRole = async (id, role) => {
    const {data} = await $authHost.patch(`api/role/${id}`, role);
    return data;
}

export const deleteRole = async (id) => {
    const {data} = await $authHost.delete(`api/role/${id}`);
    return data;
}
