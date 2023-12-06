function ApiError(status, message) {
    var error = Error.call(this, message);

    error.name = this.name = this.constructor.name;

    this.message = error.message;
    this.stack = error.stack;
    this.status = status;
}

ApiError.prototype = Object.create(Error.prototype, {
    constructor: { 
        value: ApiError,
        enumerable: false,
        writable: true,
        configurable: true, 
    }
});

ApiError.badRequest = (error) => new ApiError(404, error.stack);
ApiError.forbidden = (message) => new ApiError(403, message);

module.exports = ApiError;