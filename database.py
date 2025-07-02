from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

# Create a SQLAlchemy Engine which manages the connection pool to the database.
# `settings.database_url` is your connection string (from .env, e.g., "sqlite:///./tasks.db").
# `connect_args={"check_same_thread": False}` is required for SQLite to allow connections across threads,
# which FastAPI uses for handling requests concurrently.
engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})

# Create a SessionLocal class configured to use our engine.
# This is a factory for new database session objects (used to interact with the DB).
# `autocommit=False` means transactions won't be auto-committed.
# `autoflush=False` disables automatic flush before queries.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for our ORM models to inherit from.
# This is how SQLAlchemy knows which classes are database models when creating tables.
Base = declarative_base()
