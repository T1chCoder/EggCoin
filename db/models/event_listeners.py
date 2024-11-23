from db.models.main import *
from db.models.registration import *
from db.models.choices import *
from sqlalchemy import event
from uuid import uuid4
        
@event.listens_for(UserModel, 'before_insert')
def validate_before_insert(mapper, connection, target):
    target.validate_fields()
    
@event.listens_for(UserModel, 'before_update')
def validate_before_update(mapper, connection, target):
    target.validate_fields()
    
def assign_uuid(mapper, connection, target):
    if target.uuid is None:
        target.uuid = str(uuid4())
        
event.listen(UserModel, 'before_insert', assign_uuid)
event.listen(LoginAttemptModel, 'before_insert', assign_uuid)
event.listen(LoginFailedAttemptModel, 'before_insert', assign_uuid)
event.listen(UserProfileModel, 'before_insert', assign_uuid)
event.listen(TouchModel, 'before_insert', assign_uuid)