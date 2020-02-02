from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
distance = Table('distance', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('home_id', Integer),
    Column('category', String(length=500)),
    Column('distance_item_name', String(length=500)),
    Column('distance_in_meters', Float),
)

home = Table('home', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('id_from_website', String(length=500)),
    Column('property_name', String(length=500)),
    Column('street', String(length=500)),
    Column('region', String(length=500)),
    Column('postcode', String(length=500)),
    Column('price', Float),
    Column('including_utilies', Boolean),
    Column('area', Float),
    Column('number_of_bedrooms', Integer),
    Column('state_of_furnishing', String(length=500)),
    Column('available_from', DateTime),
    Column('offered_since', DateTime),
    Column('energy_label', String(length=500)),
    Column('description_from_tenant', String(length=500)),
    Column('tenant_contact_information', String(length=500)),
    Column('property_website_source', String(length=500)),
    Column('property_source_url', String(length=500)),
    Column('city', String(length=500)),
    Column('type_of_property', String(length=500)),
)

screenshot = Table('screenshot', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('link', String(length=500)),
    Column('home_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['distance'].create()
    post_meta.tables['home'].create()
    post_meta.tables['screenshot'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['distance'].drop()
    post_meta.tables['home'].drop()
    post_meta.tables['screenshot'].drop()
