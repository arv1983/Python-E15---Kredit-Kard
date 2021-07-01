from click import argument, echo
from flask.cli import AppGroup
from flask import Flask
from faker import Faker
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from flask_sqlalchemy import SQLAlchemy
from app.models.users import Users
from app.models.credit_cards import CreditCard
from environs import Env
from werkzeug.security import generate_password_hash, check_password_hash
from random import randrange

env = Env()
env.read_env()
fake = Faker()
fake.name()
db = SQLAlchemy()

def cli_teste(app: Flask):
    admin = AppGroup("admin")
    @admin.command("create")
    def cli_create():
        admin = fake.name()
        password = fake.password()
        data = {'login': admin,
                'password_hash': password,
                'is_admin': True}

        try:
            record_db = Users(**data)
            db.session.add(record_db)
            db.session.commit()
            echo(f"Admin criado!!")
            echo(f"login {admin}")
            echo(f"password {password}")
        except:
            echo(f"deu pau")

    user_credit_card = AppGroup("users_credit_cards")
    @user_credit_card.command("create")
    @argument("number")
    def cli_card(number: int):
        get = Users()
        max = len(get.query.all())
        
        def sorteio_user(max):
            sorteado = randrange(1, max + 1) 
            print(f'maximo {max}')
            filter = len(CreditCard().query.filter_by(user_id=sorteado).all()) 
            if filter < 2:
                print(f'sorteado {sorteado}')
                return sorteado
                
            else:
                sorteio_user(max)



        for _ in range(int(number)):

            data = {
                "expire_date": fake.credit_card_expire(),
                "number": fake.credit_card_number(),
                "provider": fake.credit_card_provider(),
                "security_code": fake.credit_card_security_code(),
                "user_id": sorteio_user(max)
            }
            
            record_db = CreditCard(**data)
            db.session.add(record_db)
            db.session.commit()            




    users = AppGroup("user")
    @users.command("create")
    @argument("number")
    def cli_create_user(number: int):
        for _ in range(int(number)):
            try:
                data = {'login': fake.name(),
                'password_hash': generate_password_hash(fake.password())
                }
                record_db = Users(**data)
                db.session.add(record_db)
                db.session.commit()
            except:
                echo(f"deu pau")


    app.cli.add_command(users)
    app.cli.add_command(admin)
    app.cli.add_command(user_credit_card)


def init_app(app: Flask):
    cli_teste(app)


