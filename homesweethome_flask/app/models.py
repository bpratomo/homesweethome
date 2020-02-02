from app import db



# Create your models here.

class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_from_website     = db.Column(db.String(500))
    property_name       = db.Column(db.String(500))
    street              = db.Column(db.String(500))
    region              = db.Column(db.String(500))
    postcode            = db.Column(db.String(500))
    price               = db.Column(db.Float())
    including_utilies   = db.Column(db.Boolean())
    area                = db.Column(db.Float())
    number_of_bedrooms  = db.Column(db.Integer())
    state_of_furnishing = db.Column(db.String(500))
    available_from      = db.Column(db.DateTime())
    offered_since       = db.Column(db.DateTime())
    energy_label        = db.Column(db.String(500))
    description_from_tenant     = db.Column(db.String(500))
    tenant_contact_information  = db.Column(db.String(500))
    property_website_source     = db.Column(db.String(500))
    property_source_url = db.Column(db.String(500))
    city                = db.Column(db.String(500))
    type_of_property    = db.Column(db.String(500))
    screenshots = db.relationship('Screenshot',backref='home',lazy='dynamic')
    distances = db.relationship('Distance',backref='home',lazy='dynamic')

    def __repr__(self):
        return '<Property %r>' % (self.property_name)
    
class Screenshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    link = db.Column(db.String(500))
    home_id = db.Column(db.Integer,db.ForeignKey('home.id'))

    def __repr__(self):
        return '<Screenshot %r>' % (self.home)

class Distance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer,db.ForeignKey('home.id'))
    category = db.Column(db.String(500))
    distance_item_name = db.Column(db.String(500))
    distance_in_meters = db.Column(db.Float())

    def __repr__(self):
        return '<Distance %r>' % (self.distance_item_name)
