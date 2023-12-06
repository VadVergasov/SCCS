var express = require('express');
var router = express.Router();

const controller = require('../controllers/userController');
const auth = require('../middlewares/checkAuthMiddleware');
const checkRole = require('../middlewares/checkRoleMiddleware');



router.post('/registration', controller.register)
router.post('/login', controller.login)

router.get('/auth', auth, controller.isAuthorized);

router.get('/', controller.getAll);
router.get('/:id', controller.getById);

router.patch('/:id', checkRole(1), controller.update);
router.delete('/:id', checkRole(1), controller.delete);

module.exports = router;