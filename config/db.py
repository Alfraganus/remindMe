from sqlalchemy import create_engine, MetaData

# engine = create_engine("mysql://root:@localhost/remind_me")
engine = create_engine("mysql://root:@localhost/remind_me")
meta = MetaData()
conn = engine.connect()