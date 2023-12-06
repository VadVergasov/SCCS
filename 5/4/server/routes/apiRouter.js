var express = require('express');
var router = express.Router();

const cardRouter = require('./cardRouter');
const authorRouter = require('./authorRouter');
const categoryRouter = require('./categoryRouter');
const userRouter = require('./userRouter');
const roleRouter = require('./roleRouter');

router.use('/card', cardRouter);
router.use('/author', authorRouter);
router.use('/category', categoryRouter);
router.use('/user', userRouter);
router.use('/role', roleRouter);

module.exports = router;