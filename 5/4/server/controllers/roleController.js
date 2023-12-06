
const ApiError = require('../errors/apiError');

const RoleRepository = require('../repositories/RoleRepository');


class RoleController {
    async create(req, res, next) {
        const {name} = req.body;

        const roleWithSameName = await RoleRepository.getByName(name);

        if (roleWithSameName) {
            return next(ApiError.badRequest("Role with same name already exists."));
        }

        const role = await RoleRepository.create({name});

        return res.json(role);
    }

    async getAll(req, res) {
        const roles = await RoleRepository.getAll();

        return res.json(roles);
    }

    async update(req, res, next) {
        try {
            const {id} = req.params;
            const {name} = req.body;

            const role = await RoleRepository.update(id, name);
      
            return res.json(role);
            
        } catch (e) {
            return next(ApiError.badRequest(e));
        }
    }

    async delete(req, res, next) {
        try {
            const {id} = req.params;
            
            const result = await CardRepository.delete(id);
        
            res.status(204).json();
        } catch (e) {
            return next(ApiError.badRequest(e));
        }
    }
}

module.exports = new RoleController();