from utils import json_read, save_to_file
import player

#convert string to json
#when 2 clients are ready, send player json

data =[{"IP":"198.0.0.1","Ready":"1"},{"IP":"198.0.0.2","Ready":"1"}]

def delete():
    pass

def string_to_json():
    save_to_file(client_response, data)