from logging import Formatter
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('myapp.log', maxBytes=10000, backupCount=1)
# creating the format for logging file
formatter = Formatter('%(asctime)s %(levelname)s %(name)s %(threadName)s %(filename)s %(funcName)s : %(message)s')

