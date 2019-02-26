# Author    kim kiogora <kimkiogora@gmail.com>
# Usage     Assessment
# Version   1.0
# Since     24 Feb 2019

from flask import Flask
import logging, ssl
import logging.handlers
from flask_restful import Api
from api import UploadCSV

app = Flask(__name__)
app.config['db_server'] = "localhost"
app.config['db_user'] = "fetti"
app.config['db_password'] = "f3tt1"
app.config['db_name'] = "assessment"
app.config['allowed_files'] = "csv"

api = Api(app)
api.add_resource(UploadCSV, '/upload')
app.config['debug_logs'] = "/var/log/tulaa/uploader_debug.log"

"""
Setup the handler
"""
handlerInfo = logging.handlers.RotatingFileHandler(app.config['debug_logs'],
                                                           maxBytes=100*1024*1024, backupCount=20)
formatter = logging.Formatter('%(asctime)s | %(name)s_%(levelname)s | %(message)s')
handlerInfo.setFormatter(formatter)
app.logger.addHandler(handlerInfo)
app.logger.setLevel(logging.DEBUG)


"""
Entry to application functionality
"""
if __name__ == "__main__":
    s_ip = "0.0.0.0"
    s_port = 8086
    app.run(debug=True, host=s_ip, port=s_port, threaded=True)

