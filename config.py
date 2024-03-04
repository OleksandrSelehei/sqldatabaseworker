from sqlalchemy.ext.asyncio import create_async_engine


# jwt
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# database
DATABASE_URL = "postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}".format(
    username="postgres",
    password="root",
    host="localhost",
    port="5432",
    database="crm",
)

engine = create_async_engine(DATABASE_URL)
