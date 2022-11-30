# from dotenv import dotenv_values
# config = dotenv_values(".env")
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/serversiderendering"

class Settings:
    DB_USER : str = os.getenv("USER_DB")
    DB_PASSWORD = os.getenv("PASS_DB")
    DB_SERVER : str = os.getenv("HOST_DB","localhost")
    DB_PORT : str = os.getenv("PORT_DB",5432) # default postgres port is 5432
    DB_DB : str = os.getenv("NAME_DB")
    # DB_URL : str = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_DB}"
    DB_URL : str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_DB}"

settings = Settings()

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://symphonious-madeleine-aa3f5d.netlify.app",
    "*",
    os.getenv("FRONTEND_URL"),
]
