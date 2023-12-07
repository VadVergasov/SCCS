import React, { useContext, useEffect, useState } from 'react';
import AuthorBar from '../components/AuthorBar';
import CategoryBar from '../components/CategoryBar';
import CardList from '../components/CardList';
import { InputGroup, Control, ErrorLabel, TextControl } from '../components/Control';
import { Context } from '../index';
import { observer } from 'mobx-react-lite';
import { getAuthors, getCards } from '../http/cardAPI';

const Museum = observer(() => {
    const {cardStore} = useContext(Context);

    const [search, setSearch] = useState("");

    useEffect(() => {
        getAuthors()
            .then(authors => {
                cardStore.setAuthors(authors);
            });

        getCards()
            .then(cards => {
                cardStore.setCards(cards.rows);
            });

        cardStore.setPattern("");
    }, []);

    return (
        <div style={{display: 'flex'}}>
            <div style={{minWidth: 'calc(100% /4)', display: 'inline-block'}}>
                <InputGroup >
                    <Control style={{width: '90%', margin: '15px'}}
                        value={search}
                        placeholder="Search"
                        onChange={ev => {setSearch(ev.target.value); cardStore.setPattern(ev.target.value);}} 
                    />
                </InputGroup>
                <div style={{display: 'flex'}}>
                    <div style={{width: 'calc(100% /2)'}}>
                        <AuthorBar />
                    </div>
                    <div style={{width: 'calc(100% /2)'}}>
                        <CategoryBar />
                    </div>
                </div>
            </div>

            <div style={{maxWidth: 'calc(100% * 3/4)'}}>
                <CardList />
            </div>
        </div>
    );
});

export default Museum;