from sqlalchemy.orm import Session
from models import Users_Table, Orders_Table
from modules import Users, Orders


# To get all user data
def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users_Table).offset(skip).limit(limit).all


# To get user by id
def get_user_by_id(db: Session, u_id: int):
    return db.query(Users_Table).filter(Users_Table.u_id == u_id).first()


# To create a new user
def create_user(db: Session, user: Users_Table):
    _user = Users_Table(name=user.u_name, email=user.u_email)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


# To delete a user
def delete_user(db: Session, u_id: int):
    _user = get_user_by_id(db=db, u_id=u_id)
    db.delete(_user)
    db.commit()


# To update user
def update_user(db: Session, u_id: int, u_name: str, u_email: str):
    _user = get_user_by_id(db=db, u_id=u_id)
    _user.u_name = u_name
    _user.u_email = u_email
    db.commit()
    db.refresh(_user)
    return _user
