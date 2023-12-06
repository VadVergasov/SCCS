import Button from '../components/Button';
import CreateRole from "../components/modals/Role/CreateRole";
import AdminCardList from "../components/tables/AdminCardList";
import EntityBar from '../components/EntityBar';
import React, { useState, useContext } from "react";
import { observer } from 'mobx-react-lite';
import { Context } from '../index';
import AdminAuthorList from '../components/tables/AdminAuthorList';
import AdminUserList from '../components/tables/AdminUserList';
import AdminCategoryList from '../components/tables/AdminCategoryList';

const Admin = observer(() => {
    const {adminStore} = useContext(Context);

    return (
        <div style={{display: 'flex', padding: '5px'}}>
            <div style={{width: 'calc(100% /4)'}}>
                <EntityBar />
            </div>

            <div style={{width: 'calc(100% * 3/4)'}}>
                {adminStore.selectedEntityId == 1
                    ? <AdminCardList />
                : adminStore.selectedEntityId == 2
                    ? <AdminAuthorList />
                : adminStore.selectedEntityId == 3
                    ? <AdminUserList />
                : adminStore.selectedEntityId == 4
                    ? <AdminCategoryList />
                :
                    <></>  
                }  
            </div>
        </div>
    )
});

export default Admin;