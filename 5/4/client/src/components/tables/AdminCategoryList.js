import { useContext, useState, useEffect } from 'react';
import styles from './AdminCategoryList.module.css';
import { Context } from '../../index';
import { observer } from 'mobx-react-lite';
import Button from '../Button';
import CreateCategory from "../modals/Category/CreateCategory";
import UpdateCategory from '../modals/Category/UpdateCategory';
import { deleteCategory, getCategories } from '../../http/cardAPI';



function CategoryItem(props) {
    const [isCategoryUpdating, setIsCategoryUpdating] = useState(false);
    const [category, setCategory] = useState(props.category || null);
    

    return (
        (category &&
            <div
                {...props} 
                className={`${styles.categoryItem} ${props.selected ? styles.selected : ''}`} 
                style={{display: 'flex', justifyContent: 'right'}}
            >
                <span style={{display: 'flex'}}>

                    <div style={{display: 'flex', whiteSpace: 'nowrap'}}>
                        <div style={{alignSelf: 'center'}}>{category.name}</div>
                    </div>
                    
                    <Button 
                        style={{width: '50%', marginLeft: '10px', background: 'red'}} 
                        onClick={() => { deleteCategory(category.id); setCategory(null); }}
                    >
                        Delete
                    </Button>

                    <Button 
                        style={{width: '95%', marginLeft: '10px', background: 'purple'}} 
                        onClick={() => setIsCategoryUpdating(true)}
                    >
                        Update
                    </Button>

                    <UpdateCategory 
                        category={category} 
                        isOpen={isCategoryUpdating} 
                        setIsOpen={setIsCategoryUpdating} 
                        reload={setCategory}
                    />
                </span>
            </div>
        )
    );
}


const AdminCategoryList = observer(() => {
    const [isCategoryCreating, setIsCategoryCreating] = useState(false);

    const {cardStore} = useContext(Context);
    
    useEffect(() => {
        getCategories()
            .then(categories => {
                cardStore.setCategories(categories);
            });
    }, []);

    return (
        <div style={{display: 'block'}}>
            {cardStore.categories.map(c => 
                <CategoryItem 
                    key={c.id} 
                    category={c}
                />
            )}

            <Button style={{width: '95%', background: 'cornflowerblue'}} onClick={() => {setIsCategoryCreating(true)}}>
                Add category
            </Button>

            <CreateCategory isOpen={isCategoryCreating} setIsOpen={setIsCategoryCreating} />
        </div>
    );
});

export default AdminCategoryList;