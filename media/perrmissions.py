from django.contrib.auth.models import Group


class CheckGroupPermissions:
    def is_in_group(user, group_name):
        try:
            return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
        except Group.DoesNotExist:
            return False