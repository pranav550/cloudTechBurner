from google.cloud import storage

client = storage.Client()
bucket_name = "client-library-bucket18sept" # Replace [my-bucket-name] with actual bucket name

if not client.bucket(bucket_name).exists():
    bucket = client.create_bucket(bucket_name)
    print(f'Bucket {bucket.name} created.')
else:
    print(f'Bucket {bucket_name} already exists.')