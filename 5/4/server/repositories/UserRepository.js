const pool = require('../db');


const roleIdToCamelCase = (user) => {
    user.roleId = user.role_id; 
    delete user.role_id; 
    return user;
}



class UserRepository {

    static async create(user) {
        return new Promise(function (resolve, reject) {
            const {login, password, roleId} = user;
            

            pool.query(
                String.raw
                    `INSERT INTO users (login, password, "role_id")  
                     VALUES ('${login}', '${password}', '${roleId}') RETURNING *`,
                (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows.map(roleIdToCamelCase)[0]);
                    } else {
                        reject(new Error("No results found"));
                    }
                }   
            );
        });
    };


    static async getAll(roleId) {
        try {
            return await new Promise(function (resolve, reject) {
                let query = roleId 
                    ? String.raw`SELECT * FROM users u WHERE u."role_id" = ${roleId}`
                    : String.raw`SELECT * FROM users u`;

                pool.query(query, (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows.map(roleIdToCamelCase));
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
        if (!id || !/^[0-9]*$/.test(`${id}`)) {
            throw new Error("No id");
        }

        try {
            return await new Promise(function (resolve, reject) {
                let query = String.raw`SELECT * FROM users u WHERE u."id" = '${id}'`

                pool.query(query, (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows.map(roleIdToCamelCase)[0]);
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


    static async getByLogin(login) {
        if (!login) {
            throw new Error("No login");
        }

        try {
            return await new Promise(function (resolve, reject) {
                let query = String.raw`SELECT * FROM users u WHERE u."login" = '${login}'`

                pool.query(query, (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    if (results && results.rows) {
                        resolve(results.rows.map(roleIdToCamelCase)[0]);
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


    static async update(id, user) {
        return new Promise(function (resolve, reject) {
            const {login, password, roleId} = user;
            const fields = {login, password, role_id: roleId};

            let query = "UPDATE users SET";

            for (let field in fields) {
                if (fields[field]) {
                    query += String.raw` "${field}" = '${fields[field]}',`;
                } else if (fields[field] === null) {
                    query += String.raw` "${field}" = NULL,`;
                }
            }

            if (query.endsWith(',')) {
                query = query.slice(0, -1);
            }

            query += ` WHERE id = ${id} RETURNING *`;

            pool.query(query, (error, results) => {
                if (error) {
                    reject(error);
                }
                if (results && results.rows) {
                    resolve(results.rows.map(roleIdToCamelCase)[0]);
                } else {
                    reject(new Error("No results found"));
                }
            });
        });
    };

    static async delete(id) {
        return new Promise(function (resolve, reject) {
            pool.query(
                `DELETE FROM users WHERE id = ${id}`,
                (error, results) => {
                    if (error) {
                        reject(error);
                    }
                    
                    resolve(`User deleted with ID: ${id}`);
                }
            );
        });
    };

}


module.exports = UserRepository;