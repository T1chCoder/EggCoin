from db.models import main as models
import sqlmodel as sql
from datetime import datetime
from uuid import uuid4

class LoginAttemptModel(sql.SQLModel, table=True):
    __tablename__ = "login_attempts"
    # ID's
    id: int = sql.Field(title="ID", primary_key=True, nullable=False)
    uuid: str = sql.Field(title="UUID", default=lambda: str(uuid4()), nullable=False)
    # Body
    user_id: int = sql.Field(title="User", foreign_key="users.id", nullable=False)
    # Links
    user: "models.UserModel" = sql.Relationship(back_populates="login_attempts", cascade_delete=True)
    # Timestamps
    created_at: datetime = sql.Field(title="Created", default=datetime.utcnow, nullable=False)
    
    def update_timestamp(self):
        self.updated_at = datetime.utcnow()

    def save(self, session: sql.Session):
        if self.id is not None:
            raise ValueError("Updating this model is not allowed.")
        session.add(self)
        session.commit()

    def __str__(self):
        return f"LoginAttempt {self.id}"

class LoginFailedAttemptModel(sql.SQLModel, table=True):
    __tablename__ = "login_failed_attempts"
    # ID's
    id: int = sql.Field(title="ID", primary_key=True, nullable=False)
    uuid: str = sql.Field(title="UUID", default=lambda: str(uuid4()), nullable=False)
    # Body
    user_id: int = sql.Field(title="User", foreign_key="users.id", nullable=False)
    # Links
    user: "models.UserModel" = sql.Relationship(back_populates="login_failed_attempts", cascade_delete=True)
    # Timestamps
    created_at: datetime = sql.Field(title="Created", default=datetime.utcnow, nullable=False)
    
    def update_timestamp(self):
        self.updated_at = datetime.utcnow()

    def save(self, session: sql.Session):
        if self.id is not None:
            raise ValueError("Updating this model is not allowed.")
        session.add(self)
        session.commit()

    def __str__(self):
        return f"LoginFailedAttempt {self.id}"