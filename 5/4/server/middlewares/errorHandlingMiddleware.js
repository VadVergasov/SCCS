function errorHandler(err, req, res, next) {
  const isDev = (process.env.NODE_ENV || 'development') === 'development';
  
  const message = err.message;
  const status = (isDev && err.status) ? err.status : 500;
  const stack = isDev ? err.stack : null;

  //const cleanedError = {message, status, stack};

  return res.status(status).json({message: message});

//  res.render('error', cleanedError);
}

module.exports = errorHandler;