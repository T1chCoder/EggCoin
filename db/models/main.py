import sqlmodel as sql
from datetime import datetime
from uuid import uuid4
import re
from . import validators, choices, registration as rgr

# Models
class UserModel(sql.SQLModel, table=True):
    __tablename__ = "users"
    # ID's
    id: int = sql.Field(title="ID", primary_key=True, nullable=False)
    uuid: str = sql.Field(title="UUID", default=lambda: str(uuid4()), nullable=False)
    tg_id: int = sql.Field(title="Tg-ID", unique=True, nullable=True)
    # Body
    username: str = sql.Field(title="Username", max_length=150, unique=True, nullable=False)
    name: str = sql.Field(title="Name", max_length=150, nullable=False)
    surname: str = sql.Field(title="Surname", max_length=150, nullable=True)
    email: str = sql.Field(title="Email", max_length=250, unique=True, nullable=True)
    photo: str = sql.Field(title="Photo", max_length=250, nullable=True)
    birthday: datetime = sql.Field(title="Birthday", nullable=True)
    age: int = sql.Field(title="Age", ge=0, nullable=True)
    # Statuses
    is_superuser: bool = sql.Field(title="Admin", default=False, nullable=False)
    is_staff: bool = sql.Field(title="Employee", default=False, nullable=False)
    is_premium: bool = sql.Field(title="Premium", default=False, nullable=False)
    is_active: bool = sql.Field(title="Active", default=True, nullable=False)
    # Activities
    is_online: bool = sql.Field(title="Online", default=False, nullable=False)
    is_offline: bool = sql.Field(title="Offline", default=False, nullable=False)
    is_dormant: bool = sql.Field(title="Dormant", default=False, nullable=False)
    # Security and Verification
    password: str = sql.Field(title="Password Hash", nullable=False)
    email_verified: bool = sql.Field(title="Email Verified", default=False, nullable=False)
    phone_verified: bool = sql.Field(title="Phone Verified", default=False, nullable=False)
    # Soft Deletion
    is_deleted: bool = sql.Field(title="Deleted", default=False, nullable=False)
    # Links
    user_profiles: list["UserProfileModel"] = sql.Relationship(back_populates="users", cascade_delete=True)
    login_attempts: list["LoginAttemptModel"] = sql.Relationship(back_populates="users", cascade_delete=True)
    login_failed_attempts: list["LoginFailedAttemptModel"] = sql.Relationship(back_populates="users", cascade_delete=True)
    # Timestamps
    last_login: datetime = sql.Field(title="Last login", nullable=True)
    updated_at: datetime = sql.Field(title="Updated", default=datetime.utcnow, nullable=False)
    created_at: datetime = sql.Field(title="Created", default=datetime.utcnow, nullable=False)
    # Constraints for field consistency
    __constraints__ = [
        sql.CheckConstraint('age >= 0', name='age_check'),
    ]

    def set_statuses(self):
        if self.is_deleted:
            self.is_online = False
            self.is_offline = False
            self.is_dormant = False
        else:
            if not any([self.is_online, self.is_offline, self.is_dormant]):
                self.is_online = True 
    
    def set_last_login(self):
        self.last_login = datetime.utcnow()

    def validate_fields(self):
        if self.email and not validators.email(self.email):
            raise ValueError("Invalid email format.")
        if self.photo and not validators.url(self.photo):
            raise ValueError("Invalid photo URL.")
        if self.password and len(self.password) < 8:  # Simple password check for min length
            raise ValueError("Password must be at least 8 characters long.")
        if self.phone_verified and not validators.phone(self.phone_verified):
            raise ValueError("Invalid phone number format.")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not hasattr(self, 'user_profiles') or not self.user_profiles:
            self.user_profiles = [UserProfileModel(user=self)]
        
        if self.birthday:
            self.age = validators.age(self.birthday)
        
        self.set_statuses()

    def __str__(self):
        return f"User {self.id}"

class LeagueModel(sql.SQLModel, table=True):
    # Table 
    __tablename__ = "leagues"
    # ID's
    id: int = sql.Field(title="ID", primary_key=True, nullable=False)
    uuid: str = sql.Field(title="UUID", default=lambda: str(uuid4()), nullable=False)
    # Body 
    owner_id: int = sql.Field(title="Owner", foreign_key="users.id", unique=True, nullable=False)
    title: str = sql.Field(title="Title", max_length=150, nullable=False)
    # Links
    owner: "UserModel" = sql.Relationship(back_populates="leagues", cascade_delete=True)
    # Timestamps
    updated_at: datetime = sql.Field(title="Updated", default=datetime.utcnow, nullable=False)
    created_at: datetime = sql.Field(title="Created", default=datetime.utcnow, nullable=False)
    
    def update_timestamp(self):
        self.updated_at = datetime.utcnow()
    
    def __str__(self):
        return f"League {self.id}"
    
# UserProfile
class UserProfileModel(sql.SQLModel, table=True):
    # Table
    __tablename__ = "user_profiles"
    # ID's
    id: int = sql.Field(title="ID", primary_key=True, nullable=False)
    uuid: str = sql.Field(title="UUID", default=lambda: str(uuid4()), nullable=False)
    # Body
    user_id: int = sql.Field(title="User", foreign_key="users.id", unique=True, nullable=False)
    language_id: int = sql.Field(title="Language", foreign_key="languages.id", nullable=False)
    league_id: int = sql.Field(title="League", foreign_key="leagues.id", nullable=True)
    coin: int = sql.Field(title="Coin", default=1, ge=1, nullable=False)
    referral_link: str = sql.Field(index=True, nullable=False)
    # Links
    user: "UserModel" = sql.Relationship(back_populates="user_profiles", cascade_delete=True)
    language: "choices.LanguageModel" = sql.Relationship(back_populates="user_profiles", cascade_delete=True)
    league: "LeagueModel" = sql.Relationship(back_populates="user_profiles", cascade_delete=True)
    touches: list["TouchModel"] = sql.Relationship(back_populates="user_profiles", cascade_delete=True)
    # Timestamps
    updated_at: datetime = sql.Field(title="Updated", default=datetime.utcnow, nullable=False)
    created_at: datetime = sql.Field(title="Created", default=datetime.utcnow, nullable=False)
    # Constraints for field consistency
    __constraints__ = [
        sql.CheckConstraint('coin >= 1', name='coin_check'),
    ]

    def update_timestamp(self):
        self.updated_at = datetime.utcnow()

    def validate_referral_link(self):
        url_regex = r"^(https?://)?([a-z0-9-]+\.)+[a-z0-9-]+(/[a-z0-9-./?%&=]*)?$"
        if not re.match(url_regex, self.referral_link):
            raise ValueError(f"Invalid URL: {self.referral_link}")
        
    def __str__(self):
        return f"UserProfile {self.id}"
    
class TouchModel(sql.SQLModel, table=True):
    # Table 
    __tablename__ = "touches"
    # ID's
    id: int = sql.Field(title="ID", primary_key=True, nullable=False)
    uuid: str = sql.Field(title="UUID", default=lambda: str(uuid4()), nullable=False)
    # Body
    user_profile_id: int = sql.Field(title="User profile", foreign_key="user_profiles.id", unique=True, nullable=False)
    taps: int = sql.Field(title="Taps", default=0, ge=1, nullable=False)
    coins: int = sql.Field(title="Coins", default=0, ge=1, nullable=False)
    # Links
    user_profile: "UserProfileModel" = sql.Relationship(back_populates="touches", cascade_delete=True)
    # Timestamps
    updated_at: datetime = sql.Field(title="Updated", default=datetime.utcnow, nullable=False)
    created_at: datetime = sql.Field(title="Created", default=datetime.utcnow, nullable=False)
    # Constraints for field consistency
    __constraints__ = [
        sql.CheckConstraint('taps >= 1', name='taps_check'),
        sql.CheckConstraint('coins >= 1', name='coins_check'),
    ]
    
    def save(self, session: sql.Session):
        self.coins = self.taps * self.user_profile.coin
        session.add(self)
        session.commit()
    
    def __str__(self):
        return f"Touch {self.id}"