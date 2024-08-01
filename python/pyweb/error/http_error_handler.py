import logging

from flask import jsonify
from werkzeug.exceptions import HTTPException

def handle_exception(error):
    logging.error(f"Error occurred: {error}", exc_info=True)

    error_dict = {"error": str(error)}

    if isinstance(error, HTTPException):
        error_dict['code'] = error.code
        error_dict['description'] = error.description
        return jsonify(error_dict), error.code

    error_dict['code'] = 500
    return jsonify(error_dict), 500