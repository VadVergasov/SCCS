import React, { useContext } from 'react';
import { Routes, Route } from 'react-router-dom';
import { authRoutes } from '../routes';
import { publicRoutes } from '../routes';
import { MUSEUM_URL } from '../utils/urls';
import { Context } from '../index';

import { observer } from 'mobx-react-lite';


const AppRouter = observer(() => {
    const {userStore} = useContext(Context);

    return (
        <Routes>
            {userStore.isAuth && Object.entries(authRoutes).map(([path, component]) => 
                <Route key={path} path={path} Component={component} exact />
            )}

            {Object.entries(publicRoutes).map(([path, component]) =>
                <Route key={path} path={path} Component={component} exact />
            )}
            
            <Route path='*' Component={publicRoutes[MUSEUM_URL]} />
        </Routes>
    );
});

export default AppRouter;