import databases
import sqlalchemy

from config import Config

database = databases.Database(Config.DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
    Config.DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
