from sqlalchemy import create_engine, String, Float, Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker
from sqlalchemy.orm import DeclarativeBase

PGUSER = 'postgres'
PGPASSWORD = '300911'

# Налаштування бази даних SQLite
engine = create_engine(f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@localhost:5432/tests.db", echo=True)
Session = sessionmaker(bind=engine)

# Базовий клас для моделей
class Base(DeclarativeBase):
    def create_db(self):
        Base.metadata.create_all(engine)

    def drop_db(self):
        Base.metadata.drop_all(engine)

class User_files(Base):
    __tablename__ = 'users_files'
    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)

b = Base()
b.create_db()