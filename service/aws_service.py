import boto3
from datetime import datetime,timezone, timedelta
def get_bucket():
    s3_client = boto3.client("s3")
    response = s3_client.list_buckets()
    buckets = response.get("Buckets", [])
    current_time =  datetime.now(timezone.utc).astimezone()
    

    print(current_time)



    old_bucket = []
    new_bucket = []
    for bucket in buckets:
        bucket_name= bucket["Name"]
        creation_date= bucket["CreationDate"]
        days_ago_90 = current_time - timedelta(days = 90)
        if creation_date <days_ago_90:
            old_bucket.append(bucket_name)
        else:
            new_bucket.append(bucket_name)

        
    return{
        "bucket_name": len(bucket),
        "new_bucket": len(new_bucket),
        "new_bucket name":new_bucket,
        "old_bucket": len(old_bucket),
        "old_bucket_name": old_bucket

     
    }
def get_ec2_instances():
    ec2_client = boto3.client("ec2")
    response = ec2_client.describe_instances()
    current_time = datetime.now(timezone.utc).astimezone()

    old_instances = []
    new_instances = []
    days_ago_90 = current_time - timedelta(days=90)

   
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            launch_time = instance["LaunchTime"]

            if launch_time < days_ago_90:
                old_instances.append(instance_id)
            else:
                new_instances.append(instance_id)
    

    return {
        "instance_count": len(old_instances) + len(new_instances),
        "new_instance_count": len(new_instances),
        "new_instance_ids": new_instances,
        "old_instance_count": len(old_instances),
        "old_instance_ids": old_instances
    }
