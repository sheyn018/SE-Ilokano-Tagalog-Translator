from . import db

class TL_IL(db.Model):
    """
    A SQLAlchemy model representing the IL to TL translation table.

    Attributes:
        id (int): Unique identifier for each translation pair.
        tl (str): Tagalog translation for a given Ilokano word.
        il (str): Ilokano word for a given Tagalog translation.
    """

    id = db.Column(db.Integer, primary_key=True)
    tl = db.Column(db.String(300))
    il = db.Column(db.String(300))

    def __repr__(self):
        """
        A string representation of the translation pair, formatted as
        "TL_IL('Tagalog translation', 'Ilokano word')".
        """
        return f"TL_IL('{self.tl}', '{self.il}')"