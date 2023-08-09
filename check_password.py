from functools import wraps
from flask import current_app
from flask import request
from flask import jsonify
import jwt


def check_password(func):
    """
    This function is used as a decorator to check the token
    """
    
    # use wraps to keep the original function name
    @wraps(func)
    def decorator(*args,**kwargs):
        x_password = None
        output_dict = dict()

        # ensure the x_password is passed with the headers
        if 'x-access-password' in request.headers:
            x_password = request.headers['x-access-password']
        if not x_password: # throw error if no token provided
            output_dict['error'] = 'x acssess password is missing!'
            return jsonify(output_dict), 401


        # check if the x_password is valid    
        if x_password != "x-access-password":
            output_dict['error'] = 'x access password is wrong!'
            return jsonify(output_dict), 401
        
        
        # call the function with its parameters
        return func(*args,**kwargs)
    return decorator
