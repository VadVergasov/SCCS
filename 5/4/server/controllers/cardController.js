const uuid = require('uuid');
const path = require('path');
const fs = require('fs');


const ApiError = require('../errors/apiError');

const pool = require('../db');

const CardRepository = require('../repositories/CardRepository');


class CardController {
    async create(req, res, next) {
        try {
            const {title, price, authorId} = req.body;

            let fname;

            try {
                if (req.files === null) {
                    fname = "image_default.jpg";
                } else {
                    const {image} = req.files;

                    const filename = uuid.v4() + '.jpg';
                    image.mv(path.resolve(__dirname, '..', 'static', filename));
    
                    fname = filename;
                }
            } catch (error) {
                fname = "image_default.jpg";
            }

            const cardWithSameTitle = await CardRepository.getByTitle(title);

            if (cardWithSameTitle) {
                return next(ApiError.badRequest(JSON.stringify({field: 'title', text: "Card with same title already exists."})));
            }

            const card = await CardRepository.create({title, price, authorId, image: fname});

            return res.json(card);
        } catch (e) {
            return next(ApiError.badRequest(e));
        }
    }

    async getAll(req, res) {
        let {authorId} = req.query;

        let cards = await CardRepository.getAll(authorId);
        cards = {rows: cards};

        return res.json(cards);
    }

    async getById(req, res) {
        const {id} = req.params;
 
        const cards = await CardRepository.getById(id);
        return res.json(cards)
    }

    async update(req, res, next) {
        try {
            const {id} = req.params;
            const newCard = {...req.body};

            try {
                if (req.files === null) {
                    
                } else {
                    const {image} = req.files;

                    const filename = uuid.v4() + '.jpg';
                    image.mv(path.resolve(__dirname, '..', 'static', filename));
    
                    newCard.image = filename;
                }
            } catch (error) {
                
            }
            
            const card = await CardRepository.update(id, newCard);

            return res.json(card);
            
        } catch (e) {
            return next(ApiError.badRequest(e));
        }
    };

    async updateCategories(req, res, next) {
        try {
            const {id} = req.params;
            const {categoriesId} = req.body;

            const newCategories = await CardRepository.updateCategories(id, categoriesId);
            return res.json(newCategories);
            
        } catch (e) {
            return next(ApiError.badRequest(e));
        }
    }

    async getCategories(req, res, next) {
        try {
            const {id} = req.params;
            
            const categories = await CardRepository.getCategories(id);
            return res.json(categories);
            
        } catch (e) {
            return next(ApiError.badRequest(e));
        }
    }

    async delete(req, res, next) {
        try {
            const {id} = req.params;

            let image = (await CardRepository.getById(id)).image;

            fs.unlink(path.resolve(__dirname, '..', 'static', image), () => {});

            const result = await CardRepository.delete(id);
        
            res.status(204).json();
        } catch (e) {
            return next(ApiError.badRequest(e));
        }
    };
}

module.exports = new CardController();