from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.services.liefecycletasks import StartupManager

class Database(StartupManager):
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = None
        self.SessionLocal = None

    @StartupManager.onStart(order=1)
    def connect(self):
        """Initialize the database connection."""
        print("Connecting to the database...")
        self.engine = create_engine(self.database_url, connect_args={"check_same_thread": False})
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        print("Database connected.")

    @StartupManager.onEnd(order=1)
    def disconnect(self):
        """Dispose of the database engine."""
        print("Closing the database connection...")
        if self.engine:
            self.engine.dispose()
            print("Database connection closed.")

    def get(self) -> Session:
        """Dependency to get a database session."""
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
