import { useContext, useState, useEffect } from 'react';
import styles from './AdminUserList.module.css';
import { Context } from '../../index';
import { observer } from 'mobx-react-lite';
import Button from '../Button';
import UpdateUser from '../modals/User/UpdateUser';
import { getUsers } from '../../http/userAPI';


function UserItem(props) {
    const [isUserUpdating, setIsUserUpdating] = useState(false);
    const [user, setUser] = useState(props.user || null);
    
    return (
        (user &&
            <div
                {...props} 
                className={`${styles.userItem} ${props.selected ? styles.selected : ''}`} 
                style={{display: 'flex', justifyContent: 'right'}}
            >
                <span style={{display: 'flex'}}>

                    <div style={{display: 'flex', whiteSpace: 'nowrap'}}>
                        <div style={{alignSelf: 'center'}}>{user.login}</div>
                    </div>

                    <Button 
                        style={{width: '95%', marginLeft: '10px', background: 'blue'}} 
                        onClick={() => setIsUserUpdating(true)}
                    >
                        Update
                    </Button>

                    <UpdateUser user={user} isOpen={isUserUpdating} setIsOpen={setIsUserUpdating} reload={setUser}/>
                    
                </span>
            </div>
        )
    );
}


const AdminUserList = observer(() => {
    const [isCardCreating, setIsCardCreating] = useState(false);

    const {userStore} = useContext(Context);

    useEffect(() => {
        getUsers()
            .then(newUsers => {
                userStore.setUsers(newUsers);
            });
    }, []);


    return (
        <div style={{display: 'block'}}>
            {userStore.users.map(u => 
                <UserItem 
                    key={u.id} 
                    user={u}
                />
            )}
        </div>
    );
});

export default AdminUserList;