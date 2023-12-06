import { useState, cloneElement, useEffect, useRef } from 'react';
import useComponentVisible from '../utils/useComponentVisible';

import styles from './Dropdown.module.css';




const Dropdown = ({ trigger, menu, closeOnClick }) => {
    const { ref, isComponentVisible: open, setIsComponentVisible: setOpen } = useComponentVisible(false);
  
    const handleOpen = () => {
        setOpen(!open);
    };
  
    return (
        <div className={styles.dropdown} ref={ref}>
            {cloneElement(trigger, {
                onClick: handleOpen,
            })}

            {open  && (
                <ul className={styles.menu}>
                    {menu.map((menuItem, index) => (
                        <li key={index} className={styles.menuItem}>
                            {cloneElement(menuItem, {
                                onClick: (e) => {
                                    menuItem.props.onClick(e);
                                    
                                    if (closeOnClick === undefined || closeOnClick === true) {
                                        setOpen(false);
                                    } 
                                },
                            })}
                        </li>
                    ))}
                </ul>
            )}
      </div>
    );
};


export default Dropdown;