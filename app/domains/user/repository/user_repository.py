from database.models.user import User

class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def create_user(self, username: str, password: str):
        user = User(
            username=username,
            hashed_password=password
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
