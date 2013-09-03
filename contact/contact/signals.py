from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from models import HistoryLog


@receiver([post_save, post_delete])
def log_history(sender, **kwargs):
    #skip logging for HistoryLog instances
    if sender is HistoryLog:
        return
    action = 'D'
    if 'created' in kwargs:
        action = 'U'
        if kwargs['created']:
            action = 'C'
    HistoryLog.objects.create(action=action, objectModel=sender.__name__)
