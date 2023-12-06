import React, { useContext, useEffect } from 'react';
import styles from './CategoryBar.module.css';
import { Context } from '../index';
import useForceUpdate from '../utils/useForceUpdate';
import { observer } from 'mobx-react-lite';
import { getCategories, getCategoryCards } from '../http/cardAPI';



function CategoryItem(props) {
    return (
        <div {...props} className={`${styles.categoryItem} ${props.selected ? styles.selected : ''}`}>
            <span>{props.name}</span>
        </div>
    );
}


const CategoryBar = observer(() => {
    const {cardStore} = useContext(Context);

    const forceUpdate = useForceUpdate();

    useEffect(() => {
        getCategories()
            .then(categories => {
                cardStore.setCategories(categories);
            })
    }, []);

    async function onChange(category) {
        const categoryCards = await getCategoryCards(category.id);
        category.cards = categoryCards;

        cardStore.selectCategory(category); 
        forceUpdate();
    }
   
    return (
        <div style={{textAlign: 'center'}}>
            <h1 style={{fontSize: '20px', fontWeight: 'bold', marginTop: '8px'}}>Categories</h1>

            <div>
                 <CategoryItem 
                    selected={null === cardStore.selectedCategory}
                    key={0} 
                    name={"All"} 
                    onClick={() => { cardStore.selectCategory(null); forceUpdate(); }} 
                />


                {cardStore.categories.map(c => 
                    <CategoryItem 
                        selected={c.id === cardStore.selectedCategory?.id}
                        key={c.id} 
                        name={c.name} 
                        onClick={async () => await onChange(c)} 
                    />
                )}
            </div> 
        </div>
    ); 
});

export default CategoryBar;