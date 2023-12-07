import { useContext, useState } from 'react';
import styles from './AdminAuthorList.module.css';
import { Context } from '../../index';
import { observer } from 'mobx-react-lite';
import Button from '../Button';
import CreateAuthor from "../modals/Author/CreateAuthor";
import UpdateAuthor from '../modals/Author/UpdateAuthor';
import { deleteAuthor } from '../../http/cardAPI';



function AuthorItem(props) {
    const [isAuthorUpdating, setIsAuthorUpdating] = useState(false);
    const [author, setAuthor] = useState(props.author || null);
    

    return (
        (author &&
            <div
                {...props} 
                className={`${styles.authorItem} ${props.selected ? styles.selected : ''}`} 
                style={{display: 'flex', justifyContent: 'right'}}
            >
                <span style={{display: 'flex'}}>

                    <div style={{display: 'flex', whiteSpace: 'nowrap'}}>
                        <div style={{alignSelf: 'center'}}>{author.name}</div>
                    </div>
                    
                    <Button 
                        style={{width: '50%', marginLeft: '10px', background: 'red'}} 
                        onClick={() => { deleteAuthor(author.id); setAuthor(null); }}
                    >
                        Delete
                    </Button>

                    <Button 
                        style={{width: '95%', marginLeft: '10px', background: 'blue'}} 
                        onClick={() => setIsAuthorUpdating(true)}
                    >
                        Update
                    </Button>

                    <UpdateAuthor author={author} isOpen={isAuthorUpdating} setIsOpen={setIsAuthorUpdating} reload={setAuthor}/>
                    
                </span>
            </div>
        )
    );
}


const AdminAuthorList = observer(() => {
    const [isAuthorCreating, setIsAuthorCreating] = useState(false);

    const {cardStore} = useContext(Context);
    const authors = cardStore.authors;

    return (
        <div style={{display: 'block'}}>
            {authors.map(a => 
                <AuthorItem 
                    key={a.id} 
                    author={a}
                />
            )}

            <Button style={{width: '95%', background: 'cornflowerblue'}} onClick={() => {setIsAuthorCreating(true)}}>
                Add author
            </Button>

            <CreateAuthor isOpen={isAuthorCreating} setIsOpen={setIsAuthorCreating} />
        </div>
    );
});

export default AdminAuthorList;