from app.routes import db, user


def create_my_user(first_name, last_name, hobbies):
    db.session.add(
        user(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies
        )
    )
    db.session.commit()


if __name__ == "__main__":
    create_my_user("Andrew", "Reynolds", "Video games")
    users = user.query.all()
    print(users)
    create_my_user("John", "Doe", "Playing golf")
    obj = user.query.filter_by(first_name="John").first()
    print(obj)
