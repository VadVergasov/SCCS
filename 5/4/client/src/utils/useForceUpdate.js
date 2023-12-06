import { useState } from 'react'


export default function useForceUpdate() {
    const [, setTick] = useState(true);
    
    const update = () => {
        setTick(value => !value);
    };

    return update;
}