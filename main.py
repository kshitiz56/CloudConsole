import aws
import config
import display

def start_func(instance_db):
    inp = input("instance:")
    if inp == "":
        return
    instance_indexes = parse_integer_string(inp)
    for inst in instance_indexes:
        instance = instance_db[working_provider][working_region][inst]
        print("Starting instance", instance['Object'].id)
        instance['Object'].start()


def stop_func(instance_db):
    inp = input("instance:")
    if inp == "":
        return
    instance_indexes = parse_integer_string(inp)
    for inst in instance_indexes:
        instance = instance_db[working_provider][working_region][inst]
        print("Stopping instance", instance['Object'].id)
        instance['Object'].stop()

def parse_integer_string(input_str):
    result = set()  # Use a set to avoid duplicates

    # Split the input string by commas
    segments = input_str.split(',')

    for segment in segments:
        if '-' in segment:
            # Handle ranges (e.g., "11-14")
            start, end = map(int, segment.split('-'))
            result.update(range(start, end + 1))
        else:
            # Handle single integers (e.g., "4")
            result.add(int(segment))

    # Convert the set to a sorted list
    return sorted(result)

def select(items, default):
    for i in range(len(items)):
        print(f"{i}. {items[i]['Name']}")
    inp = input("?:")
    if inp.isdigit():
        choice = int(inp)
        if choice not in range(len(items)):
            return default
        return choice
    return default



def update_instances():
    global custom_filter
    instance_list = {'aws': {}, 'gcp': {}}
    for region in regions['aws']:
        instance_list['aws'][region] = regions['aws'][region].list_instances(ORDER, custom_filter)
    return instance_list

def modify_filter():
    if custom_filter[0].get('Values') is not None:
        print("Current filter:" + custom_filter[0]['Values'][0])
    inp = input("?:")

    if inp == "None":
        custom_filter[0]['Values'] = []
    else :
        custom_filter[0]['Values'] = [inp]
'''
    if column_size * 2 < width:
        line1 = '-' * width
        line2 = "|{column1:^{column_size}}|{column2:^{column_size}}|".format(column1="Stopped",column2="Running", column_size=column_size)
        line3 = '-' * width
        line4 = f"|{index_str:^{index_str_size}}|{name_str:^{name_str_size}}|{index_str:^{index_str_size}}|{name_str:^{name_str_size}}|"
        line5 = '-' * width
        lines.append(line1);lines.append(line2);lines.append(line3);lines.append(line4);lines.append(line5);
    else:
        line1 = '-' * column_size
        line2 = "|{column:^{column_size}}|".format(column="Stopped", column_size=column_size)
        line3 = '-' * column_size
        line4 = f"|{index_str:^{index_str_size}}|{name_str:^{name_str_size}}|"
        line5 = '-' * column_size
        lines.append(line1); lines.append(line2); lines.append(line3); lines.append(line4); lines.append(line5)


    code1 = STOP_CODE
    code2 = RUNNING_CODE

    while True:
        instance1 = instance2 = None
        if instance_list.get(code1) is not None and len(instance_list[code1]) > 0:
            instance1 = instance_list[code1].pop()
        if instance_list.get(code2) is not None and len(instance_list[code2]) > 0:
            instance2 = instance_list[code2].pop()
        line = ""

        if instance1 is None and instance2 is None:
            break
        if instance1 is not None and instance2 is None:
            name = instance1['Name']
            index = instance1['Index']
            line = f"|{index:^{index_str_size}}|{name:<{name_str_size}}|{' ':^{index_str_size}}|{' ':^{name_str_size}}|"
        if instance1 is None and instance2 is not None:
            name = instance2['Name']
            index = instance2['Index']
            line = f"|{' ':^{index_str_size}}|{' ':^{name_str_size}}|{index:^{index_str_size}}|{name:<{name_str_size}}|"
        if instance1 is not None and instance2 is not None:
            name1 = instance1['Name']
            index1 = instance1['Index']
            name2 = instance2['Name']
            index2 = instance2['Index']
            line = f"|{index1:^{index_str_size}}|{name1:<{name_str_size}}|{index2:^{index_str_size}}|{name2:<{name_str_size}}|"
        lines.append(line)

    line6 = '-' * width
    lines.append(line6)
'''

ORDER = {"stopped": 0, "running": 1, "pending": 2, "stopping": 3, "terminated": 4}
# Define your custom filter (for example, filtering by 'Owner' tag)
#custom_filter = [{'Name': 'tag:Name', 'Values': ['*kshitiz*']}]
custom_filter = None

configuration = config.read_config()
working_provider = configuration['working_provider']
working_region = configuration['working_region']
regions = {'aws': {}, 'gcp': {}}

for region in configuration['display_regions']['aws']:
    regions['aws'][region] = aws.Aws(region)
for region in configuration['display_regions']['gcp']:
    regions['gcp'][region] = None
instance_db = update_instances()

commands = [{'Name': 'start', 'Object': start_func},
            {'Name': 'stop', 'Object': stop_func},
            {'Name': 'list', 'Object': display.display},
            {'Name': 'filter', 'Object': modify_filter}
            ]

while True:
    instance_db = update_instances()
    display.display(instance_db)
    for i in range(len(commands)):
        print(f"{i}) {commands[i]['Name']}")
    inp_str = input("?:")
    if not inp_str.isdigit():
        continue
    inp = int(inp_str)
    if inp == 2:
        continue
    commands[inp]['Object'](instance_db)

class CloudInstance():
    def __init__(self, instance):
        self.instance = instance

    def start(self):
        pass

    def stop(self):
        pass

    def terminate(self):
        pass

class AWSInstance(CloudInstance):
    def start(self):
        self.instance.start()

    def stop(self):
        #print(f"Stopping AWS instance {self.instance_id}")
        self.instance.stop()

    def terminate(self):
        self.instance.terminate()

class GCPInstance(CloudInstance):
    def start(self):
        print(f"Starting GCP instance")

    def stop(self):
        print(f"Stopping GCP instance")

    def terminate(self):
        print(f"Terminating GCP instance")

"""
ec2_client = boto3.client('ec2', region_name=region)  # Replace 'your_region' with the appropriate AWS region

response = ec2_client.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                name = tag['Value']
        instance_id = instance['InstanceId']
        state_code = instance['State']['Code']  # Integer code for the instance state
        state_name = instance['State']['Name']  # String representation of the state (e.g., 'running', 'stopped', etc.)
        print(f"{name} {state_name}")
"""
