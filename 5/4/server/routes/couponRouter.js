var express = require('express');
var router = express.Router();

const checkRole = require('../middlewares/checkRoleMiddleware');

router.get('/', controller.getAll);
router.get('/user/:id', controller.getByUserId);
router.post('/', checkRole(1), controller.create);

router.patch('/:id', checkRole(1), controller.update);
router.delete('/:id', checkRole(1), controller.delete);

module.exports = router;
