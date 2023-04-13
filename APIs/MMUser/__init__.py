from flask import Blueprint

# Blueprint creation.
auth_main = Blueprint("new_auth_main", __name__,  url_prefix='/api/v1/auth')
