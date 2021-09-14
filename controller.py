import configparser

information = configparser.ConfigParser()


def save_body_info(height, weight):
    information['BODY'] = {'Weight': weight,
                           'Height': height}
    write_config()


def write_config():
    with open('configurations.ini', 'w') as file:
        information.write(file)
