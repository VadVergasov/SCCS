import styles from "./UpdateCard.module.css";
import { useState, useContext, useEffect } from 'react';
import Modal from '../Modal';
import Button from '../../Button';
import Dropdown from '../../Dropdown';
import { InputGroup, Control, ErrorLabel, TextControl } from '../../Control';
import { Context } from '../../../index';
import { getAuthors, updateCard, getCards, getCategories, updateCardCategories, getCardCategories } from '../../../http/cardAPI';
import { observer } from 'mobx-react-lite';


const UpdateCard = observer((props) => {
    const {cardStore} = useContext(Context);
    const card = props.card || {};

    const isOpen = props.isOpen;
    const setIsOpen = props.setIsOpen;

    const [title, setTitle] = useState(card.title || "");
    const [selectedAuthor, setSelectedAuthor] = useState(cardStore.authors.find(a => a.id === card.authorId));
    const [price, setPrice] = useState(card.price || "");
    const [image, setImage] = useState("");
    // const [categories, setCategories] = useState(Object.fromEntries(getCardCategories(card.id).map(c => {
    //     return [c.id, c.name];
    // })) || {});
    const [categories, setCategories] = useState({});

    const [titleError, setTitleError] = useState("");
    const [authorError, setAuthorError] = useState("");
    const [priceError, setPriceError] = useState("");

    useEffect(() => {
        getAuthors()
            .then(authors => {
                cardStore.setAuthors(authors);
            });

        getCategories()
            .then(categories => {
                cardStore.setCategories(categories);
            })

        getCardCategories(card.id)
            .then(categories => {
                setCategories(Object.fromEntries((categories).map(c => {
                    return [c.id, c.name];
                })))
            })
    }, [props]);


    const selectFile = (e) => {
        setImage(e.target.files[0]);
    }

    const addCategory = (category) => {
        setCategories({...categories, [category.id]: category.name})
    }

    const removeCategory = (category) => {
        let newCategories = {...categories};
        delete newCategories[category.id];
        setCategories(newCategories);
    }

    function onUpdate() {
        var isError = false;

        if (!titleError) {
            if (title === "") {
                setTitleError("Enter card title");
                isError = true;
            } else {
                setTitleError("");
            }
        } else {
            isError = true;
        }

        if (!authorError) {
            if (selectedAuthor === null) {
                setAuthorError("Select author");
                isError = true;
            } else {
                setAuthorError("");
            }
        } else {
            isError = true;
        }

        if (!priceError) {
            if (price === null) {
                setPriceError("Enter card price");
                isError = true;
            } else {
                setPriceError("");
            }
        } else {
            isError = true;
        }

        if (isError) {
            return;
        }

        const formData = new FormData();
        formData.append('title', title);
        formData.append('authorId', `${selectedAuthor.id}`);
        formData.append('price', `${price}`);

        if (image !== "") {
            formData.append('image', image);
        }

        updateCard(card.id, formData)
            .then(newCard => {
                updateCardCategories(newCard.id, Object.keys(categories))
                    .then(newCardCategories => {});

                if (props.reload) {
                    props.reload(newCard);
                }

                getCards()
                    .then(cards => {
                        cardStore.setCards(cards.rows);
                    });

                setTitle(newCard.title);
                setSelectedAuthor(cardStore.authors.find(a => a.id === newCard.authorId));
                setPrice(newCard.price);
                setImage("");

                setTitleError("");
                setAuthorError("");
                setPriceError("");

                setIsOpen(false);
            })
            .catch(e => {
                setTitleError(JSON.stringify(e));
                console.log(e);
            });
    }

    function onCancel() {
        setTitle(card.title);
        setSelectedAuthor(cardStore.authors.find(a => a.id === card.authorId));
        setPrice(card.price);
        setImage("");
        setCategories({});

        setTitleError("");
        setAuthorError("");
        setPriceError("");

        setIsOpen(false);
    }
    

    return (
        <Modal isOpen={isOpen} setIsOpen={setIsOpen} onClose={onCancel}>
            <div>
                <div className={styles.header}>
                    <h5 className={styles.heading}>Update card</h5>
                </div>
            
                <div className={styles.content}>
                    <InputGroup>
                        <Control
                            value={title}
                            placeholder="Change card title"
                            onChange={ev => {setTitle(ev.target.value); setTitleError("");}} 
                        />
                        <ErrorLabel>{titleError}</ErrorLabel>
                    </InputGroup>

                    <InputGroup>
                        <Dropdown
                            trigger={<Control
                                value={selectedAuthor?.name ?? ''}
                                placeholder="Change card author"
                                readOnly={true}
                                style={{cursor: 'pointer'}} 
                            />}

                            menu={cardStore.authors.map(a => {
                                return (
                                    <button onClick={() => { setSelectedAuthor(a); setAuthorError("")}}>
                                        {a.name}
                                    </button>
                                )
                            })}
                        />
                        <ErrorLabel>{authorError}</ErrorLabel>
                    </InputGroup>

                    <InputGroup>
                        <Dropdown
                            trigger={<Control
                                value={Object.values(categories).join()}
                                placeholder="Select card categories"
                                readOnly={true}
                                style={{cursor: 'pointer'}} 
                            />}

                            menu={cardStore.categories.map(c => {
                                return (
                                    <button 
                                        onClick={() => {(c.id in categories) ? removeCategory(c) : addCategory(c)}} 
                                        style={{background: (c.id in categories ? 'gray' : 'inherit')}}
                                    >
                                        {c.name}
                                    </button>
                                )
                            })}

                            closeOnClick={false}
                        />
                    </InputGroup>

                    <InputGroup style={{marginTop: '20px'}}>
                        <Control
                            type="number"
                            min="0" max="1000" 
                            value={price}
                            placeholder="Change card price"
                            onChange={ev => { setPrice(+ev.target.value); setPriceError("")}} 
                        />
                        <ErrorLabel>{priceError}</ErrorLabel>
                    </InputGroup>

                    <InputGroup style={{marginTop: '20px'}}>
                        <Control
                            type="file"
                            placeholder="Change card image"
                            onChange={ev => {setImage(ev.target.value); selectFile(ev)}} 
                        />
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

export default UpdateCard;
