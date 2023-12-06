import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getCard } from '../http/cardAPI';

const CardDetails = () => {
    const [card, setCard] = useState({});
    const {id} = useParams();

    useEffect(() => {

        getCard(id)
            .then(card => {
                setCard(card);
            });

    }, [])

    return (
        <div style={{display: 'flex'}}>
            <div style={{width: 'calc(100% /2)'}}>
                <div style={{padding: '25px'}}>
                    <img 
                        src={process.env.REACT_APP_API_URL + card.image} 
                        alt={card.title} 
                        style={{borderRadius: '20px', width: '100%'}}
                    />
                </div>
                
            </div>

            <div style={{width: 'calc(100% /2)'}}>
                <div style={{padding: '25px'}}>
                    <h1 style={{marginBottom: '45px'}}>{card.title}</h1>
                    {<p style={{fontSize: '30px'}}>Price: {card.price}</p>}
                    
                </div>
            </div>
        </div>
    );
}

export default CardDetails;