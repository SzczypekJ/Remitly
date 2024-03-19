import json

# Function to check if the input JSON Resource field contains a single asterisk.
# Returns False if it contains an asterisk, True otherwise.
# Exceptions occur when:
# 1. The JSON file is not found.
# 2. The JSON file has a bad format.
# 3. The JSON data does not contain the necessary fields - Resource field.


def check_json_file(file_path):
    try:
        # Opening the file with JSON data
        with open(file_path, 'r') as f:
            # Loading the JSON data from the file
            data = json.load(f)
            # Check if the JSON is empty and if we have the 'PolicyDocument' field in data.
            # If it is empty or we don't have the 'PolicyDocument' field, we return False because we don't have the 'Resource' field (exception)
            if not data or 'PolicyDocument' not in data:
                return False
            # Check if the JSON has the 'Statement' field.
            # If it doesn't, we return False because we don't have the 'Resource' field (exception)
            if 'Statement' not in data['PolicyDocument']:
                return False

            # Loop through each statement in the 'Statement'
            for statement in data['PolicyDocument']['Statement']:
                # Check if the JSON has the 'Resource' field.
                # If it doesn't, we return False because we don't have the 'Resource' field (exception)
                if 'Resource' not in statement:
                    return False
                # Got the statement with key == Resource and get the value from this key
                # and assign it to the new variable resource
                resource = statement['Resource']
                # Checking if the value is str and if this value is equal to '*'
                if isinstance(resource, str) and resource == '*':
                    # If it is, we return False
                    return False

    # Checking if the file exists. If not, we return False (exception)
    except FileNotFoundError:
        return False
    # Checking if the JSON file has a good format. If not, we return False (exception)
    except json.JSONDecodeError:
        return False

    # Return True in any other cases
    return True


# Example usage:
json_file_path = 'C:/Users/szczy/Desktop/STUDIA/dodat/Remitly/data.json'
result = check_json_file(json_file_path)
print(result)
