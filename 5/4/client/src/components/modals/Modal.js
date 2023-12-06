import styles from "./Modal.module.css";
import Button from '../Button';


const Modal = (props) => {
    const isOpen = props.isOpen;
    const setIsOpen = props.setIsOpen;

    const onClose = props.onClose || (() => {});

    return (
        <> 
            {isOpen && 
                <div>
                    <div className={styles.darkBG} onClick={() => { setIsOpen(false); onClose();}} />
                    
                    <div className={styles.centered}>
                        <div className={styles.modal}> 
                            <Button 
                                className={styles.closeBtn} 
                                onClick={() => {setIsOpen(false); onClose();}} 
                                style={{background: '#ff4050'}}
                            >
                                X
                            </Button>

                            {props.children}
                        </div>
                    </div>
                </div>
            }
        </>
    );
};

export default Modal;