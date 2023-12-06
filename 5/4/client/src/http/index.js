import axios from 'axios';


const $host = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    withCredentials: false,
        headers: {
          'Access-Control-Allow-Origin' : '*',
          'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',   
      }
});


const $authHost = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    withCredentials: false,
        headers: {
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',   
        }
});

const authInterceptor = (config) => {
    config.headers.authorization = `Bearer ${localStorage.getItem('token')}`;
    return config;
}


$authHost.interceptors.request.use(authInterceptor);

export {
    $host,
    $authHost,
}