import sys

from app.dependencies import engine
from app.models.user import Base


def main():
    try:
        print("🔧 Initializing database...")
        Base.metadata.create_all(bind=engine)
        print("✅ Tables created successfully!")
    except Exception as e:
        print(
            f"❌ An error occurred while creating tables: {str(e)}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
