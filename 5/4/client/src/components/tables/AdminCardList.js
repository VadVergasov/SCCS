import { useContext, useState, useEffect } from 'react';
import styles from './AdminCardList.module.css';
import { Context } from '../../index';
import { observer } from 'mobx-react-lite';
import Button from '../Button';
import UpdateCard from '../modals/Card/UpdateCard';
import { getAuthors, getCards,  createCard } from '../../http/cardAPI';
import { deleteCard } from '../../http/cardAPI';
import CreateCard from "../modals/Card/CreateCard";


function CardItem(props) {
    const [isCardUpdating, setIsCardUpdating] = useState(false);
    const [card, setCard] = useState(props.card || null);
    

    return (
        (card &&
            <div
                {...props} 
                className={`${styles.cardItem} ${props.selected ? styles.selected : ''}`} 
                style={{display: 'flex', justifyContent: 'space-between'}}
            >
                <img 
                    src={process.env.REACT_APP_API_URL + card.image} 
                    alt={`${card.title}`} 
                    style={{height: '100px', borderRadius: '15px', display: 'flex'}}
                />
                <span style={{display: 'flex'}}>

                    <div style={{display: 'flex', whiteSpace: 'nowrap'}}>
                        <div style={{alignSelf: 'center'}}>{card.title}</div>
                    </div>
                    
                    <Button 
                        style={{width: '50%', marginLeft: '10px', background: 'red'}} 
                        onClick={() => { deleteCard(card.id); setCard(null); }}
                    >
                        Delete
                    </Button>

                    <Button 
                        style={{width: '95%', marginLeft: '10px', background: 'purple'}} 
                        onClick={() => setIsCardUpdating(true)}
                    >
                        Update
                    </Button>

                    <UpdateCard card={card} isOpen={isCardUpdating} setIsOpen={setIsCardUpdating} reload={setCard}/>
                    
                </span>
            </div>
        )
    );
}


const AdminCardList = observer(() => {
    const [isCardCreating, setIsCardCreating] = useState(false);

    const {cardStore} = useContext(Context);

    useEffect(() => {
        getAuthors()
            .then(authors => {
                cardStore.setAuthors(authors);
            });

        getCards()
            .then(newCards => {
               cardStore.setCards(newCards.rows);
            });
    }, []);


    return (
        <div style={{display: 'block'}}>
            {cardStore.cards.map(b => 
                <CardItem 
                    key={b.id} 
                    card={b}
                />
            )}

            <Button style={{width: '95%', background: 'cornflowerblue'}} onClick={() => {setIsCardCreating(true)}}>
                Add card
            </Button>

            <CreateCard isOpen={isCardCreating} setIsOpen={setIsCardCreating} />
        </div>
    );
});

export default AdminCardList;