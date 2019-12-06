from table import Column, Integer, Text, MetaData, Table

metadata = MetaData()
devices = Table(
    'messages', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text),
    Column('rssi', Integer),                 
)

messages.create(bind=engine)