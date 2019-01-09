from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'))
    menu = db.relationship('MenuModel')

    def __init__(self, name, price, menu_id):
        self.name = name
        self.price = price
        self.menu_id = menu_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'menu_id': self.menu_id}

    @classmethod
    def find_by_name(cls, name):
        # SELECT * FROM items WHERE name=name, 1st row
        return ItemModel.query.filter_by(name=name).first()
        # possible bug fix
        # return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
