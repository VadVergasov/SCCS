const ApiError = require('../errors/apiError');

const CategoryRepository = require('../repositories/CategoryRepository');


class CategoryController {
    async create(req, res, next) {
        const {name} = req.body;

        const categotyWithSameName = await CategoryRepository.getByName(name);

        if (categotyWithSameName) {
            return next(ApiError.badRequest("Author with same name already exists."));
        }

        const category = await CategoryRepository.create({name});

        return res.json(category);
    }

    async getAll(req, res) {
        const categories = await CategoryRepository.getAll();
        return res.json(categories);
    }

    async getCards(req, res, next) {
        try {
            const {id} = req.params;
            
            const cards = await CategoryRepository.getCards(id);
            return res.json(cards);
            
        } catch (e) {
            return next(ApiError.badRequest(e));
        }
    }

    async update(req, res, next) {
        try {
            const {id} = req.params;
            const {name} = req.body;

            const category = await CategoryRepository.update(id, name);
                
            return res.json(category);
            
        } catch (e) {
            return next(ApiError.badRequest(e));
        }
    }

    async delete(req, res, next) {
        try {
            const {id} = req.params;
            
            const result = await CategoryRepository.delete(id);
        
            res.status(204).json();
        } catch (e) {
            return next(ApiError.badRequest(e));
        }
    }
}

module.exports = new CategoryController();