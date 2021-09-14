import configparser

information = configparser.ConfigParser()


def save_body_info(height, weight):
    information['BODY'] = {'Weight': weight,
                           'Height': height}
    write_config()


def read_config(file_name='configurations.ini'):
    with open(file_name, 'r') as file:
        information.read(file_name)
    return information['BODY']['Weight'], information['BODY']['Height']


def write_config(file_name='configurations.ini'):
    with open(file_name, 'w') as file:
        information.write(file)
