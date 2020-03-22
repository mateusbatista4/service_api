from flask import Flask
from datetime import datetime
from flask_restful import Resource, Api,fields,marshal_with,reqparse
from .models import NotificationModel
from .http_status import HttpStatus
from pytz import utc

class NotificationManager():

    last_id = 0

    def __init__(self):
        self.notifications = {}

    def insert_notification(self,notification):
        self.__class__.last_id +=1
        notification.id = self.__class__.last_id
        self.notifications[self.__class__.last_id] = notification

    def get_notification(self,id):
        return self.notifications[id]

    def delete_notifications(self,id):
        del self.notifications[id]


notification_fields = {
    'id':fields.Integer,
    'uri':fields.Url('notification_endpoint'),
    'message':fields.String,
    'ttl':fields.Integer,
    'creation_date':fields.DateTime,
    'notification_category':fields.String,
    'displayed_times' : fields.Integer,
    'displayed_once':fields.Boolean
}

notification_manager = NotificationManager()