from flask import Blueprint

# Blueprint creation.
package_main = Blueprint("new_package_name", __name__,  url_prefix='/api/v1/application')
