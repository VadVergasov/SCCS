import { $host, $authHost } from './index';


export const createCard = async (card) => {
    try {
        const {data} = await $authHost.post('api/card', card);
        return data;
    } catch (e) {
        let fieldError;

        try {
            fieldError = JSON.parse(e?.response?.data?.message)
        } catch (jsonError) {            
            throw (e?.response?.data?.message);
        }

        throw fieldError;
    }
}

export const getCards = async (authorId) => {
    const res = await $host.get('api/card', { params: {authorId}});

    const {data} = res;
    return data;
}


export const getCard = async (id) => {
    const {data} = await $host.get(`api/card/${id}`);
    return data;
}


export const updateCard = async (id, card) => {
    const {data} = await $authHost.patch(`api/card/${id}`, card);
    return data;
}

export const getCardCategories = async (id) => {
    const {data} = await $host.get(`api/card/${id}/categories`)
    return data;
}

export const getCategoryCards = async (id) => {
    const {data} = await $host.get(`api/category/${id}/cards`)
    return data;
}


export const updateCardCategories = async (id, categoriesId) => {
    const {data} = await $authHost.post(`api/card/${id}/categories`, {categoriesId})
    return data;
}

export const deleteCard = async (id) => {
    const {data} = await $authHost.delete(`api/card/${id}`);
    return data;
}



export const createAuthor = async (name) => {
    const {data} = await $authHost.post('api/author', {name});
    return data;
}

export const getAuthors = async () => {
    const {data} = await $host.get('api/author');
    return data;
}

export const updateAuthor = async (id, author) => {
    const {data} = await $authHost.patch(`api/author/${id}`, author);
    return data;
}

export const getAuthorCards = async (id) => {
    const {data} = await $host.get(`api/author/${id}/cards`)
    return data;
}

export const deleteAuthor = async (id) => {
    const {data} = await $authHost.delete(`api/author/${id}`);
    return data;
}



export const createCategory = async (name) => {
    const {data} = await $authHost.post('api/category', {name});
    return data;
}

export const getCategories = async () => {
    const {data} = await $host.get('api/category');
    return data;
}

export const updateCategory = async (id, category) => {
    const {data} = await $authHost.patch(`api/category/${id}`, category);
    return data;
}

export const deleteCategory = async (id) => {
    const {data} = await $authHost.delete(`api/category/${id}`);
    return data;
}


