import styles from "./UpdateCategory.module.css";
import { useState, useContext, useEffect } from 'react';
import Modal from '../Modal';
import Button from '../../Button';
import { InputGroup, Control, ErrorLabel } from '../../Control';
import { updateCategory } from "../../../http/cardAPI";
import { observer } from 'mobx-react-lite';
import { Context } from '../../../index';
import { getCategoris, updateCard, getCards } from '../../../http/cardAPI';


const UpdateCategory = observer((props) => {
    const isOpen = props.isOpen;
    const setIsOpen = props.setIsOpen;
    const {cardStore} = useContext(Context);
    const category = props.category || {};

    const [name, setName] = useState(category.name || "");
    const [nameError, setNameError] = useState("");

    
    function onUpdate() {
        if (name === "") {
            setNameError("Enter category name");
            return;
        }

        updateCategory(category.id, {name})
            .then(newCategory => {
                if (props.reload) {
                    props.reload(newCategory)
                }

                setName(newCategory.name);
                setNameError("");
                setIsOpen(false);
            })
            .catch(e => {
                setNameError(JSON.stringify(e));
            });
    }

    function onCancel() {
        setName(category.name);
        setNameError("");
        setIsOpen(false);
    }

    return (
        <Modal isOpen={isOpen} setIsOpen={setIsOpen} onClose={onCancel}>
            <div>
                <div className={styles.header}>
                    <h5 className={styles.heading}>Update category</h5>
                </div>
            
                <div className={styles.content}>
                    <InputGroup>
                        <Control
                            value={name}
                            placeholder="Change category name"
                            onChange={ev => {setName(ev.target.value); setNameError("");}} 
                        />
                        <ErrorLabel>{nameError}</ErrorLabel>
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


export default UpdateCategory;
