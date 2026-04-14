import logging
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.config import Config as conf


logger = logging.getLogger(__name__)
Base = declarative_base()


class DatabaseConnection:
    """
    Database connection manager that confugures the engine and session
    """

    _engine = None
    _sessionmaker = None

    @classmethod
    def get_engine(cls):
        """
        Get engine from config
        """
        if cls._engine is None:
            logger.debug(f"Engine installation...")
            cls._engine = create_engine(conf.SQLITE_DB_LINK, echo=False)
            logger.info(f"Engine installed: '{cls._engine}'.")
        return cls._engine

    @classmethod
    def get_sessionmaker(cls):
        """
        Get session factory on engine
        """
        if cls._sessionmaker is None:
            logger.debug(f"Session installation...")
            cls._sessionmaker = sessionmaker(
                bind=cls.get_engine(),
                autocommit=False,
                autoflush=False,
            )
            logger.info(f"Sessionmaker installed.")
        return cls._sessionmaker

    @classmethod
    def init_db(cls):
        """
        Create database tables
        """
        logger.info(f"Database tables created.")
        Base.metadata.create_all(bind=cls.get_engine())

    @classmethod
    def close(cls):
        """
        Close all session and clear engine
        """
        if cls._engine:
            logger.debug(f"Closing all connections...")
            cls._engine.dispose()
            cls._engine = None
            cls._sessionmaker = None

        logger.info(f"Connetion was closed.")

    @classmethod
    @contextmanager
    def session_scope(cls):
        """
        Managing database interactions
        """
        factory = cls.get_sessionmaker()
        session = factory()

        try:
            yield session
            logger.debug(f"Applying changes...")
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"Rollback changes! Error: {e}.")
            raise
        finally:
            session.close()
