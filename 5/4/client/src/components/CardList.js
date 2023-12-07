import { useContext } from 'react';
import styles from './CardList.module.css';
import { Context } from '../index';
import { useNavigate } from 'react-router-dom';
import { CARD_URL } from '../utils/urls';
import { observer } from 'mobx-react-lite';


function CardItem(props) {
    const navigate = useNavigate();

    return (
        <div 
            {...props} 
            className={`${styles.cardItem} ${props.selected ? styles.selected : ''}`} 
            onClick={() => navigate(CARD_URL.replace(':id', props.card.id))}
            style={{display: 'grid', alignItems: 'end'}}
        >
            <img 
                src={process.env.REACT_APP_API_URL + props.card.image} 
                alt={`${props.card.title}`} 
                style={{width: '100%', borderRadius: '15px'}}
            />
            <div>
                <p style={{whiteSpace: 'nowrap', margin: '10px', fontSize: '1.5em '}}>{props.card.title}</p>
                <p style={{fontWeight: 'bold', margin: '10px'}}>{props.card.price}</p>
            </div>
        </div>
    );
}


const CardList = observer(() => {
    const {cardStore} = useContext(Context);
    let cards = cardStore.cards;
    const pattern = cardStore.pattern;
    const selectedAuthor = cardStore.selectedAuthor;
    const selectedCategory = cardStore.selectedCategory;

    cards = cards.filter(b => (pattern === "")
                            ? true
                            : b.title.toUpperCase().startsWith(pattern.toUpperCase()));
    
    cards = cards.filter(b => selectedAuthor ? b.authorId == selectedAuthor?.id : true);


    if (selectedCategory && Object.keys(selectedCategory).length) {
        cards = cards.filter(b => (selectedCategory?.id && selectedCategory.cards) 
            ? selectedCategory.cards.map(b => b.id).includes(b.id) 
            : true);
    }

    if (selectedAuthor && Object.keys(selectedAuthor).length) {
        cards = cards.filter(b => (selectedAuthor?.id && selectedAuthor.cards) 
            ? selectedAuthor.cards.map(b => b.id).includes(b.id) 
            : true);
    }

    return (
        <div style={{display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)'}}>
            {cards.map(b => 
                <CardItem 
                    key={b.id} 
                    card={b}
                />
            )}
        </div>
    );
});

export default CardList;