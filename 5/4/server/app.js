var createError = require('http-errors');
var express = require('express');

var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
require('dotenv').config({ debug: true });

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var testAPIRouter = require('./routes/testAPI');
var apiRouter = require('./routes/apiRouter');

const cors = require('cors');
const fileUpload = require('express-fileupload');

const errorHandler = require('./middlewares/errorHandlingMiddleware');

var app = express();

const origin = process.env.BASE_URL || 'http://localhost:3001';
app.use(cors({origin: origin}));

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.static(path.resolve(__dirname, 'static')));
app.use(fileUpload({}));
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

app.use('/testAPI', testAPIRouter);
app.use('/api', apiRouter);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
// app.use(function(err, req, res, next) {
//   res.render('error', errorHandler(err, req, res, next));
// });

app.use(errorHandler);


module.exports = app;
