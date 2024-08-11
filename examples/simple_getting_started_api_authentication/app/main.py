from fastapi import FastAPI, Depends, HTTPException, status, Header
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from keycove import hash, generate_token
from sqlalchemy.orm import Session

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite3"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ApiKey(Base):
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True, autoincrement=True)
    hashed_key = Column(String, nullable=False, unique=True)


Base.metadata.create_all(bind=engine)


def verify_api_key(api_key: str = Header(None), db: Session = Depends(get_db)) -> None:
    """
    This function verifies the provided API key by hashing it and checking if the hashed key exists in the database.
    If the hashed key does not exist in the database, it raises an HTTPException with a 404 status code.

    Parameters:
    api_key (str): The API key to verify. This is expected to be provided in the request header.
    db (Session): The database session to use for querying the database.

    Raises:
    HTTPException: If the provided API key is not valid.
    """

    api_key = db.query(ApiKey).filter(ApiKey.hashed_key == hash(api_key)).first()
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The provided API key is not valid. Please provide a valid API key.",
        )


@app.get("/protected")
def protected_route(verify_api_key: None = Depends(verify_api_key)):
    """
    This function is a protected route that requires a valid API key to access.
    If the API key is valid, it returns a message indicating that access has been granted.

    Parameters:
    verify_api_key (None): This is a dependency that ensures the API key is verified before the function is accessed.

    Returns:
    dict: A dictionary with a message indicating that access has been granted.
    """

    return {"message": "access granted"}


@app.post("/create_api_key")
def create_api_key(db: Session = Depends(get_db)):
    """
    This function creates a new API key, hashes it, encrypts it, and stores it in the database.
    It then returns the new API key.

    Parameters:
    db (Session): The database session to use for querying the database.

    Returns:
    dict: A dictionary with the new API key.
    """

    new_key = generate_token()
    hashed_key = hash(new_key)
    api_key = ApiKey(hashed_key=hashed_key)

    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return {"api_key": new_key}


@app.get("/api_keys")
def get_api_keys(db: Session = Depends(get_db)):
    """
    This function retrieves all the hashed keys from the database.

    Parameters:
    db (Session): The database session to use for querying the database.

    Returns:
    dict: A dictionary with all the hashed keys.
    """

    api_keys = db.query(ApiKey).all()
    return {"api_keys": [api_key.hashed_key for api_key in api_keys]}
