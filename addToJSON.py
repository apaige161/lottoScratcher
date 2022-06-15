

import json
# add logic into a function 

def addTicketToJSON(new_data, filename):
    with open(filename,'r+') as file:
        jsonStr = json.dumps(new_data.__dict__)
        # Load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["ky"].append(jsonStr)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)