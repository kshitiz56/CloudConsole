import os
STOP_CODE = 80
RUNNING_CODE = 16
PENDING_CODE = 0
STOPPING_CODE = 64
TERMINATED_CODE = 48

DISPLAY_COLUMNS = ["Idx", "Name", "PublicIp"]
PRINT_TABLES = {STOP_CODE: "Stopped", RUNNING_CODE: "Running",
                    PENDING_CODE: "Pending", STOPPING_CODE: "Stopping", TERMINATED_CODE: "Terminated"}
tables = {}

for table in PRINT_TABLES.keys():
    tables[table] = PRINT_TABLES[table]

def get_column_lines(index_str, index_str_size, name_str, name_str_size,
                     column_size, instance_list, code, code_name, min_entries):
    lines = []
    line1 = '-' * column_size
    line2 = "|{column:^{column_size}}|".format(column=code_name, column_size=(column_size-2))
    line3 = '-' * column_size
    line4 = f"|{index_str:^{index_str_size}}|{name_str:^{name_str_size}}|"
    line5 = '-' * column_size
    lines.append(line1); lines.append(line2); lines.append(line3); lines.append(line4); lines.append(line5)

    entries = 0
    if instance_list.get(code) is not None:
        for instance in instance_list[code]:
            name = instance['Name']
            index = instance['Index']
            line = f"|{index:^{index_str_size}}|{name:<{name_str_size}}|"
            lines.append(line)
            entries += 1

    if min_entries is not None:
        while entries < min_entries:
            line = f"|{' ':^{index_str_size}}|{' ':<{name_str_size}}|"
            lines.append(line)
            entries += 1

    line6 = '-' * column_size
    lines.append(line6)

    return lines

def display_instances(instances):
    #global instances
    #instances = update_instances()

    instance_list = {}
    max_name_size = 0
    #for instance in instances:
    for i in range(len(instances)):
        #instance_list.append({'Name': instance['Name'], 'State': instance['Object'].state['Name']})
        code = instances[i]['Object'].state['Code']
        if instance_list.get(code) is None:
            instance_list[code] = []
        info = {'Index': i, 'Name': instances[i]['Name']}
        for column in DISPLAY_COLUMNS:
            if column == "PublicIp":
                info[column] = instances[i]['Object'].public_ip_address
            if column == "Idx":
                info[column] = i
            if column == "Name":
                info[column] = instances[i]['Name']

        instance_list[code].append(info)

        if len(instances[i]['Name']) > max_name_size:
            max_name_size = len(instances[i]['Name'])

    size = os.get_terminal_size()
    width = size.columns
    half_width = int(width/2)

    lines = []
    index_str = "Idx"; index_str_size = len(index_str) + 2
    name_str = "Name"; name_str_size = max(max_name_size + 1, len(name_str))
    column_size = index_str_size + name_str_size + 3

    tables_keys = []
    for key in tables.keys():
        if instance_list.get(key) is not None:
            tables_keys.append(key)

    i = 0
    while i < len(tables_keys):
        if (i + 1) < len(tables_keys) and (column_size * 2) < width:
            min_entries = max(len(instance_list[tables_keys[i]]), len(instance_list[tables_keys[i+1]]))
            lines_tmp_1 = get_column_lines(index_str, index_str_size, name_str, name_str_size,
                                 column_size, instance_list, tables_keys[i], tables[tables_keys[i]], min_entries)
            lines_tmp_2 = get_column_lines(index_str, index_str_size, name_str, name_str_size,
                                 column_size, instance_list, tables_keys[i+1], tables[tables_keys[i+1]], min_entries)
            if len(lines_tmp_1) != len(lines_tmp_2):
                print("ERROR")
            for j in range(len(lines_tmp_1)):
                lines.append(f"{lines_tmp_1[j]:^{half_width}}{lines_tmp_2[j]:^{half_width}}")
            i += 2
        else:
            lines_tmp_1 = get_column_lines(index_str, index_str_size, name_str, name_str_size,
                     column_size, instance_list, tables_keys[i], tables[tables_keys[i]], None)
            for j in range(len(lines_tmp_1)):
                lines.append(f"{lines_tmp_1[j]:^{half_width}}")

            i += 1
    for line in lines:
        print(line)

def display(instance_db):
    for region in instance_db['aws']:
        display_instances(instance_db['aws'][region])