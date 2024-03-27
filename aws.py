import boto3

class Aws():
    def __init__(self, region):
        self.region = region
        self.resource = boto3.resource('ec2', region_name=region)

    def list_instances(self, ORDER, filter=None):
        #     = ec2_resource.instances.filter(Filters=custom_filter)
        if filter is not None:
            instance_collection = self.resource.instances.filter(Filters=filter)
        else:
            instance_collection = self.resource.instances.all()
        instance_list = []
        for instance in instance_collection:
            name = None
            if instance.tags is None:
                print("Warning: Instance doesn't have tags " + instance.id)
                name = instance.id
            else:
                for tag in instance.tags:
                    if tag['Key'] == 'Name':
                        name = tag['Value']
                if name is None:
                    print("Warning: Instance doesn't have Name tag " + instance.id)
                    name = instance.id
            instance_list.append({'Name': name, 'Object': instance})

        # Sort instances by state
        instance_list = sorted(instance_list, key=lambda instance: ORDER[instance['Object'].state['Name']])

        return instance_list
