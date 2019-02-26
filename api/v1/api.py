from flask import request
from flask_restful import Resource
from flask import current_app as app
from datetime import datetime
import time
from Algorithms import Algos
from DBConnector import Connector
import csv
import io
from werkzeug.utils import secure_filename

class UploadCSV(Resource):
    def __init__(self):
        self.connector = Connector(app.config['db_server'], app.config['db_user'], 
                app.config['db_password'],app.config['db_name'])
        self.alg = Algos()
        super(UploadCSV, self).__init__()

    ''' Format CSV file '''
    def transform(self, text_file_contents):
        return text_file_contents.replace("=", ",")


    ''' Get value from object '''
    def get_value(self, row, item):
        value = None
        try:
            value = row[item]
            if value == '':
                value = None
        except:
            pass
        return value
    
    '''
        Data -> 'first_name, last_name, date_of_birth, postal_address, national_id, gender
    '''
    def generate_values(self, csv_file):
        data = {}
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile,  delimiter=',')
            for row in reader:
                data['first_name'] = self.get_value(row, 'first_name')
                data['last_name'] = self.get_value(row,'last_name')
                data['date_of_birth'] = self.get_value(row, 'date_of_birth')
                data['postal_address'] = self.get_value(row, 'postal_address')
                data['national_id'] = self.get_value(row, 'national_id')
                data['gender'] = self.get_value(row, 'gender')
        return data

    ''' Accept post requests '''
    def post(self):
        self.alg.write_log(app, "POST | UploadCSV| begin processing xxx", "info")
        f = request.files['csv_file']
        if not f:
            self.alg.write_log(app, "No file found", "error")
            return {'status': 201, 'message': "No file"}, 500
        
        if not self.alg.allowed_file(f.filename):
            self.alg.write_log(app, "Invalid file found", "error")
            return {'status': 201, 'message': "Only CSV files allowed"}, 500
        
        filename = secure_filename(f.filename)
        
        actual_data = self.generate_values(filename)
        national_id = actual_data['national_id']
        if national_id is None:
            return {'status': 201, 'message': "national_id is empty or missing"}, 500

        first_name = actual_data['first_name']
        if first_name is None:
            return {'status': 201, 'message': "first_name is empty or missing"}, 500
        
        last_name = actual_data['last_name']
        if last_name is None:
            return {'status': 201, 'message': "last_name is empty or missing"}, 500
        
        date_of_birth = actual_data['date_of_birth']
        if date_of_birth is None:
            return {'status': 201, 'message': "date_of_birth is empty or missing"}, 500
        
        postal_address = actual_data['postal_address']
        if postal_address is None:
            return {'status': 201, 'message': "postal_address is empty or missing"}, 500

        gender = actual_data['gender']
        if gender is None:
            return {'status': 201, 'message': "gender is empty or missing"}, 500

        self.alg.write_log(app, "Actual Data is %r" % actual_data, "info")
        
        '''Insert into database'''
        _ins_sql = "INSERT IGNORE into profile (national_id, first_name, last_name,date_of_birth,gender,postal_addres,created,modified) VALUES ('%s','%s','%s','%s','%s','%s',now(),now())" \
                % (national_id, first_name, last_name, date_of_birth, gender, postal_address) 
        self.alg.write_log(app,"INSERT SQL -> %s" % _ins_sql, "info")
        
        result = self.connector.do_insert(_ins_sql)

        self.alg.write_log(app, "Ran insert query, result is %s" % str(result), "info")

        resp = {
                'status': '200',
                'message': 'Uploaded'
                }
        return resp
