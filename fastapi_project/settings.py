from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings configuration.
    
    This class defines all the configuration parameters for the application,
    including application name, version, debug mode, server settings, and database configuration.
    """
    # Application configuration
    APP_NAME: str = "FastAPI Project"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Server configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Database configuration (for future use)
    DATABASE_URL: str = "sqlite:///./app.db"

    class Config:
        """
        Pydantic configuration class.
        
        Specifies that environment variables should be loaded from the .env file.
        """
        env_file = ".env"


settings = Settings()
