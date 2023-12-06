const pool = require('../db');


const authorIdToCamelCase = (card) => {
    card.authorId = card.author_id; 
    delete card.author_id; 
    return card;
}

const cardCategoryToCamelCase = (cardCategory) => {
    cardCategory.cardId =  cardCategory.card_id;
    cardCategory.categoryId =  cardCategory.category_id;

    delete cardCategory.card_id; 
    delete cardCategory.category_id;
    
    return cardCategory;
}


class CardRepository {

    static async create(card) {
        return new Promise(function (resolve, reject) {
            const {title, price, authorId, image} = card;

            pool.query(
                String.raw
                    `INSERT INTO cards (title, price, "author_id", image)  
                     VALUES ('${title}', ${price}, '${authorId}', '${image}') RETURNING *`,
                (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows.map(authorIdToCamelCase)[0]);
                    } else {
                        reject(new Error("No results found"));
                    }
                }   
            );
        });
    };


    static async getAll(authorId) {
        try {
            return await new Promise(function (resolve, reject) {
                let query = authorId 
                    ? String.raw`SELECT * FROM cards b WHERE b."author_id" = '${authorId}'`
                    : String.raw`SELECT * FROM cards b`;

                pool.query(query, (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows.map(authorIdToCamelCase));
                    } else {
                        reject(new Error("No results found"));
                    }
                });
            });
        } catch (error_1) {
            console.error(error_1);
            throw new Error("Internal server error");
        }
    };


    static async getById(id) {
        if (!id) {
            throw new Error("No id");
        }

        try {
            return await new Promise(function (resolve, reject) {
                let query = String.raw`SELECT * FROM cards b WHERE b."id" = ${id}`

                pool.query(query, (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows.map(authorIdToCamelCase)[0]);
                    } else {
                        reject(new Error("No results found"));
                    }
                });
            });
        } catch (error_1) {
            console.error(error_1);
            throw new Error("Internal server error");
        }
    };


    static async getByTitle(title) {
        if (!title) {
            throw new Error("No title");
        }

        try {
            return await new Promise(function (resolve, reject) {
                let query = String.raw`SELECT * FROM cards b WHERE b."title" = '${title}'`

                pool.query(query, (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows.map(authorIdToCamelCase)[0]);
                    } else {
                        reject(new Error("No results found"));
                    }
                });
            });
        } catch (error_1) {
            console.error(error_1);
            throw new Error("Internal SERWE error");
        }
    };


    static async update(id, card) {
        return new Promise(function (resolve, reject) {
            const {title, price, authorId, image} = card;
            const fields = {title, price, author_id: authorId, image};

            let query = "UPDATE cards SET";

            for (let field in fields) {
                if (fields[field]) {
                    query += String.raw` "${field}" = '${fields[field]}',`;
                }
            }

            if (query.endsWith(',')) {
                query = query.slice(0, -1);
            }

            query += ` WHERE id = ${id} RETURNING *`;

            console.log(query);

            pool.query(query, (error, results) => {
                if (error) {
                    reject(error);
                }
                if (results && results.rows) {
                    resolve(results.rows.map(authorIdToCamelCase)[0]);
                } else {
                    reject(new Error("No results found"));
                }
            });
        });
    };


    static async updateCategories(id, categoriesId) {
        return new Promise(function (resolve, reject) {
            let query = String.raw`DELETE FROM cards_categories WHERE card_id = ${id};`

            if (categoriesId.length) {
                
                query += `INSERT INTO cards_categories (card_id, category_id) VALUES`
            
                categoriesId.forEach(categoryId => {
                    query += ` (${id}, ${categoryId}),`
                });

                if (query.endsWith(',')) {
                    query = query.slice(0, -1);
                }

                query += String.raw`;`
            }

            console.log(query);

            pool.query(query, (error, results) => {
                if (error) {
                    reject(error);
                }else {
                    resolve(true);
                } 
            });
            
        });
    }

    static async getCategories(id) {
        return new Promise(function (resolve, reject) {
            let query = String.raw
            `SELECT 
                c.id AS id,
                c.name AS name
                
                FROM cards_categories bc
                     JOIN cards b ON bc.card_id = b.id AND b.id = '${id}'
                     JOIN categories c ON bc.category_id = c.id;`;

            pool.query(query, (error, results) => {
                if (error) {
                    reject(error);
                }
                if (results && results.rows) {
                    resolve(results.rows);
                } else {
                    reject(new Error("No results found"));
                }
            });
        });
    }

    static async delete(id) {
        return new Promise(function (resolve, reject) {
            pool.query(
                `DELETE FROM cards WHERE id = ${id}`,
                (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    
                    resolve(`Card deleted with ID: ${id}`);
                }
            );
            
        });
    };
}


module.exports = CardRepository;