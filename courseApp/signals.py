# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model

# User = get_user_model()

# @receiver(post_save, sender=User)
# def create_admin_user(sender, instance=None, created=False, **kwargs):
#     """
#     Create an admin user if none exists
#     """
#     if created:
#         # Check if this is the first user being created
#         if User.objects.count() == 1:
#             # Make the first user an admin
#             instance.is_admin = True
#             instance.is_staff = True
#             instance.is_superuser = True
#             instance.save()

