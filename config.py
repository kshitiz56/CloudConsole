import configparser

def create_config():
    config = configparser.ConfigParser()

    # Add sections and key-value pairs
    config['General'] = {'debug': True, 'log_level': 'info'}
    config['Database'] = {'db_name': 'example_db', 'db_host': 'localhost', 'db_port': '5432'}

    # Write the configuration to a file
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def read_config():
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('/Users/kbartariya/.cloudconsole.ini')

    # Access values from the configuration file
    working_region = config.get('working', 'region').strip()
    working_provider = config.get('working', 'provider').strip()
    aws_regions = config.get('aws', 'regions')
    gcp_regions = config.get('gcp', 'regions')

    aws_regions = aws_regions.strip().split(',')
    aws_regions = [x.strip() for x in aws_regions]

    gcp_regions = gcp_regions.strip().split(',')
    gcp_regions = [x.strip() for x in gcp_regions]

    if working_provider == "aws":
        if working_region not in aws_regions:
            aws_regions.append(working_region)
    elif working_provider == "gcp":
        if working_region not in gcp_regions:
            gcp_regions.append(working_region)
    else:
        print("Unknown cloud provider: " + working_provider)

    # Return a dictionary with the retrieved values
    config_values = {
        'working_region': working_region,
        'working_provider': working_provider,
        'display_regions': {"aws": aws_regions, "gcp": gcp_regions},
    }
    return config_values