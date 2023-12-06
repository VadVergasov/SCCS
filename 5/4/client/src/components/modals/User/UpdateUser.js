import styles from "./UpdateUser.module.css";
import { useState, useContext, useEffect } from 'react';
import Modal from '../Modal';
import Button from '../../Button';
import Dropdown from '../../Dropdown';
import { InputGroup, Control, ErrorLabel, TextControl } from '../../Control';
import { Context } from '../../../index';
import { getUsers } from '../../../http/userAPI';
import { updateUser, getRoles } from '../../../http/userAPI';
import { observer } from 'mobx-react-lite';


const UpdateUser = observer((props) => {
    const {userStore} = useContext(Context);
    const user = props.user || {};

    const isOpen = props.isOpen;
    const setIsOpen = props.setIsOpen;

    let [selectedRole, setSelectedRole] = useState(userStore.roles.find(r => r.id === user.roleId));
    const [roleError, setRoleError] = useState("");


    useEffect(() => {
        getRoles()
            .then(roles => {
                userStore.setRoles(roles);
                setSelectedRole(userStore.roles.find(r => r.id === user.roleId));
            });

    }, [props]);




    function onUpdate() {
        if (selectedRole.id == 3) {
            selectedRole.id = 1;
        }

        let newUser = {roleId: selectedRole.id}
        updateUser(user.id, newUser)
            .then(newUser => {
                if (props.reload) {
                    props.reload(newUser);
                }

                getUsers()
                    .then(users => {
                        userStore.setUsers(users);
                    });

                setIsOpen(false);
            })
            .catch(e => {
                setRoleError(e?.response?.data?.message);
                console.log(e);
            });
    }

    function onCancel() {
        setSelectedRole(userStore.roles.find(r => r.id == user.roleId));
        setRoleError("");

        setIsOpen(false);
    }
    

    return (
        <Modal isOpen={isOpen} setIsOpen={setIsOpen} onClose={onCancel}>
            <div>
                <div className={styles.header}>
                    <h5 className={styles.heading}>Update user</h5>
                </div>
            
                <div className={styles.content}>
                    <InputGroup>
                        <Dropdown
                            trigger={<Control
                                value={selectedRole?.name ?? ''}
                                placeholder="Change user role"
                                readOnly={true}
                                style={{cursor: 'pointer'}} 
                            />}
                        />
                        <ErrorLabel>{roleError}</ErrorLabel>
                    </InputGroup>

                </div>
                <div className={styles.actions}>
                    <div className={styles.container}>
                        <Button className={styles.btn} style={{background: '#13a4FD'}} onClick={onUpdate}>
                            Save
                        </Button>
                        <Button className={styles.btn} style={{background: '#ff4050'}} onClick={onCancel}>
                            Cancel
                        </Button>
                    </div>
                </div>
            </div>
        </Modal>
    )
});

export default UpdateUser;
