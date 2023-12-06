var express = require('express');
var router = express.Router();

const controller = require('../controllers/cardController');
const checkRole = require('../middlewares/checkRoleMiddleware');

router.get('/', controller.getAll);
router.get('/:id', controller.getById);
router.get('/:id/categories', controller.getCategories)

router.post('/', checkRole(1), controller.create);
router.patch('/:id', checkRole(1), controller.update);

router.post('/:id/categories', checkRole(1), controller.updateCategories)

router.delete('/:id', checkRole(1), controller.delete);

module.exports = router;