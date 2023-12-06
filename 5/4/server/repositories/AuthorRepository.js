const pool = require('../db');


class AuthorRepository {

    static async create(author) {
        return new Promise(function (resolve, reject) {
            const {name} = author;

            pool.query(
                String.raw
                    `INSERT INTO authors (name)  
                     VALUES ('${name}') RETURNING *`,
                (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows[0]);
                    } else {
                        reject(new Error("No results found"));
                    }
                }   
            );
        });
    };


    static async getAll() {
        try {
            return await new Promise(function (resolve, reject) {
                let query = String.raw`SELECT * FROM authors`;

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
                let query = String.raw`SELECT * FROM authors a WHERE a."id" = ${id}`

                pool.query(query, (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows[0]);
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


    static async getByName(name) {
        if (!name) {
            throw new Error("No NAME");
        }

        try {
            return await new Promise(function (resolve, reject) {
                let query = String.raw`SELECT * FROM authors a WHERE a."name" = '${name}'`

                pool.query(query, (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows[0]);
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


    static async update(id, name) {
        return new Promise(function (resolve, reject) {
            if (!name) {
                reject(new Error("No name"));
            }

            let query = `UPDATE authors SET name = '${name}' WHERE id = ${id} RETURNING *`;

            pool.query(query, (error, results) => {
                if (error) {
                    reject(error);
                }
                if (results && results.rows) {
                    resolve(results.rows[0]);
                } else {
                    reject(new Error("No results found"));
                }
            });
        });
    };


    static async delete(id) {
        return new Promise(function (resolve, reject) {
            pool.query(
                `DELETE FROM authors WHERE id = ${id}`,
                (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    
                    resolve(`Author deleted with ID: ${id}`);
                }
            );
        });
    };

    static async getCards(id) {
        return new Promise(function (resolve, reject) {
            let query = String.raw
            `SELECT 
                b.id AS id,
                b.title AS title,
                b.author_id AS authorId,
                b.price AS price,
                b.image AS image
            
                FROM cards b 
                    JOIN authors a ON b.author_id = a.id AND a.id = '${id}';`;

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

}


module.exports = AuthorRepository;