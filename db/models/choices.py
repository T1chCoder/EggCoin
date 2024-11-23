import sqlmodel as sql
from db.models import main as models
from datetime import datetime
from uuid import uuid4

class LanguageModel(sql.SQLModel, table=True):
    __tablename__ = "languages"
    # ID's
    id: int = sql.Field(title="ID", primary_key=True, nullable=False)
    uuid: str = sql.Field(title="UUID", default=lambda: str(uuid4()), nullable=False)
    # Body
    title: str = sql.Field(title="Title", max_length=250, nullable=False)
    # Links
    user_profiles: list["models.UserProfileModel"] = sql.Relationship(back_populates="languages", cascade_delete=True)
    # Timestamps
    updated_at: datetime = sql.Field(title="Updated", default=datetime.utcnow, nullable=False)
    created_at: datetime = sql.Field(title="Created", default=datetime.utcnow, nullable=False)

    def update_timestamp(self):
        self.updated_at = datetime.utcnow()
        
    def __str__(self):
        return f"Language {self.id}"