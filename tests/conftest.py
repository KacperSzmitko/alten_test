import pytest
import os
from fastapi.testclient import TestClient
from testcontainers.postgres import PostgresContainer
from sqlmodel import Session, create_engine
from app.main import app
from alembic import command
from alembic.config import Config
from app.dependencies import db


@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:16") as postgres:
        postgres.start()
        yield postgres


@pytest.fixture(scope="session")
def db_engine(postgres_container):
    engine = create_engine(postgres_container.get_connection_url())
    yield engine
    engine.dispose()


@pytest.fixture(scope="session")
def db_session(db_engine):
    with Session(db_engine) as session:
        yield session


@pytest.fixture(scope="session", autouse=True)
def run_migrations(postgres_container):
    """Run Alembic migrations on the test database."""
    # Get the base directory (backend) where alembic.ini is located
    alembic_ini_path = "alembic.ini"

    # Set environment variables for Alembic to connect to the test database
    os.environ["DATABASE_URL"] = (
        f"postgresql://{postgres_container.username}:{postgres_container.password}@{postgres_container.get_container_host_ip()}:{postgres_container.get_exposed_port(5432)}/{postgres_container.dbname}"
    )

    # Configure Alembic with the correct path
    alembic_cfg = Config(str(alembic_ini_path))

    # Override the script_location setting to ensure it uses the correct directory
    alembic_cfg.set_main_option("script_location", "alembic")

    # Run migrations
    command.upgrade(alembic_cfg, "head")
    yield


@pytest.fixture
def client(db_session):
    # Override the DB dependency
    def override_get_session():
        yield db_session

    app.dependency_overrides[db.get_session] = override_get_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
