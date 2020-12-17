from datetime import datetime

from taqueriaposapp.extensions import db


class ResourceMixin(object):
    """
    Global save & delete model functions.
    keep track when records are created and updated.
    """
    created_on = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_on = db.Column(
        db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())

    def save(self):
        """
        Save a model instance
        return: Model instance
        """
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """
        Delete a model instance
        return: db.session.commit()'s result
        """
        db.session.delete(self)
        return db.session.commit()
