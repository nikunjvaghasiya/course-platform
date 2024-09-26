import cloudinary
from decouple import config
# CLOUDINARY_URL=cloudinary://897976599224998:wDYXZNWs_NoNt8fMQPfLgDSERmo@dxj8ujqmr

CLOUDINARY_CLOUD_NAME = config("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_CLOUD_API_KEY = config("CLOUDINARY_CLOUD_API_KEY")
CLOUDINARY_CLOUD_API_SECRET = config("CLOUDINARY_CLOUD_API_SECRET")


def cloudinary_init():
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLOUD_NAME, 
        api_key = CLOUDINARY_CLOUD_API_KEY, 
        api_secret = CLOUDINARY_CLOUD_API_SECRET,
        secure=True
    )