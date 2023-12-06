import styles from "./UpdateAuthor.module.css";
import { useState, useContext, useEffect } from 'react';
import Modal from '../Modal';
import Button from '../../Button';
import { InputGroup, Control, ErrorLabel } from '../../Control';
import { updateAuthor } from "../../../http/cardAPI";
import { observer } from 'mobx-react-lite';
import { Context } from '../../../index';
import { getAuthors, updateCard, getCards } from '../../../http/cardAPI';


const UpdateAuthor = observer((props) => {
    const isOpen = props.isOpen;
    const setIsOpen = props.setIsOpen;
    const {cardStore} = useContext(Context);
    const author = props.author || {};

    const [name, setName] = useState(author.name || "");
    const [nameError, setNameError] = useState("");

    function onUpdate() {
        if (name === "") {
            setNameError("Enter author name");
            return;
        }

        updateAuthor(author.id, {name})
            .then(newAuthor => {
                if (props.reload) {
                    props.reload(newAuthor)
                }

                setName(newAuthor.name);
                setNameError("");
                setIsOpen(false);
            })
            .catch(e => {
                setNameError(JSON.stringify(e));
            });
    }

    function onCancel() {
        setName(author.name);
        setNameError("");
        setIsOpen(false);
    }

    return (
        <Modal isOpen={isOpen} setIsOpen={setIsOpen} onClose={onCancel}>
            <div>
                <div className={styles.header}>
                    <h5 className={styles.heading}>Update author</h5>
                </div>
            
                <div className={styles.content}>
                    <InputGroup>
                        <Control
                            value={name}
                            placeholder="Change author name"
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


export default UpdateAuthor;
