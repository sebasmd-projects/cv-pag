import os
from datetime import date
from PIL import Image


def optimize_image(sender, instance, *args, **kwargs):
    """
    This function is used as a signal handler for the post_save signal of a model with an profile_photo field. 
    It opens the image file, saves it with a quality of 40 and optimizes the image.
    """
    if instance.profile_photo:
        profile_photo = Image.open(
            instance.profile_photo.path
        )
        profile_photo.save(
            instance.profile_photo.path,
            quality=40,
            optimize_image=True
        )


def avatar_directory_path(instance, filename):
    """
    This function is used to generate a file path for an avatar image when a user is saved. 
    The path includes the current year, month, and day, as well as the full name of the user and the original filename of the image.
    """
    return f"user/{instance.id} - {instance.get_full_name()}/avatar/{date.today().year}-{date.today().month}-{date.today().day}/{filename}"


def auto_delete_profile_photo_on_delete(sender, instance, *args, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `UserModel` object is deleted.
    """
    if instance.profile_photo:
        if os.path.isfile(instance.profile_photo.path):
            os.remove(instance.profile_photo.path)


def auto_delete_profile_photo_on_change(sender, instance, *args, **kwargs):
    """
    Deletes old file from filesystem when corresponding `UserModel` object is updated with new file.
    """
    if instance.pk:  # Check if the instance is already saved (i.e., has a primary key)
        try:
            old_instance = sender.objects.get(pk=instance.pk)  # Get the old instance
        except sender.DoesNotExist:
            return  # If old instance doesn't exist, do nothing
        if old_instance.profile_photo != instance.profile_photo:  # Check if profile photo has changed
            if old_instance.profile_photo:  # Check if there was an old profile photo
                if os.path.isfile(old_instance.profile_photo.path):  # Check if old file exists
                    os.remove(old_instance.profile_photo.path)  # Delete old file

