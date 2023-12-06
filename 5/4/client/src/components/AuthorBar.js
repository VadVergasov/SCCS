import React, { useContext, useEffect } from 'react';
import styles from './AuthorBar.module.css';
import { Context } from '../index';
import useForceUpdate from '../utils/useForceUpdate';
import { observer } from 'mobx-react-lite';
import { getAuthors, getAuthorCards } from '../http/cardAPI';


function AuthorItem(props) {
    return (
        <div {...props} className={`${styles.authorItem} ${props.selected ? styles.selected : ''}`}>
            <span>{props.name}</span>
        </div>
    );
}


const AuthorBar = observer(() => {
    const {cardStore} = useContext(Context);

    const forceUpdate = useForceUpdate();

    useEffect(() => {
        getAuthors()
            .then(author => {
                cardStore.setAuthors(author);
            })
    }, []);

    async function onChange(author) {
        const authorCards = await getAuthorCards(author.id);
        author.cards = authorCards;

        cardStore.selectAuthor(author); 
        forceUpdate();
    }

    return (
        <div style={{textAlign: 'center'}}>
            <h1 style={{fontSize: '20px', fontWeight: 'bold', marginTop: '8px'}}>Authors</h1>

            <div>
                 <AuthorItem 
                    selected={null === cardStore.selectedAuthor}
                    key={0} 
                    name={"All"} 
                    onClick={() => { cardStore.selectAuthor(null); forceUpdate(); }} 
                />


                {cardStore.authors.map(a => 
                    <AuthorItem 
                        selected={a.id === cardStore.selectedAuthor?.id}
                        key={a.id} 
                        name={a.name} 
                        onClick={async () => { await onChange(a); }} />
                )}
            </div> 
        </div>
    ); 
});

export default AuthorBar;