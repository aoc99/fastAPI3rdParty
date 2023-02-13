import datetime, os
from dotenv import load_dotenv
from typing import Optional
import stringcase

load_dotenv()
expired = datetime.timedelta(minutes=30)
private_key = None
public_key = None

with open("oauth-private.key") as f:
    private_key = f.read()
with open("oauth-public.key") as  f:
    public_key = f.read()

class Config:
    DEBUG=False
    ERROR_INCLUDE_MESSAGE=False
    
    HOST=os.getenv("HOST", "127.0.0.1")
    NAME="DigiLoan API"
    PORT=os.getenv("PORT", 80)
    
    APP_URL=os.getenv("APP_URL")
    APIKEY=os.getenv("APIKEY")
    BACKEND_URL=os.getenv("BACKEND_URL")
    BACKEND_URL_MESRA = os.getenv("BACKEND_URL_MESRA")
    LOAN_CORE_URL=os.getenv("LOAN_CORE_URL")
    
    CLIENT_ID=os.getenv("CLIENT_ID", os.urandom(32))
    SECRET_KEY=os.getenv("SECRET_KEY", os.urandom(16))

    # SESSION_COOKIE_DOMAIN=APP_URL.replace("/api", "")
    # SESSION_COOKIE_PATH="/"
    # SESSION_COOKIE_SAMESITE="lax"
    
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_POOL_SIZE=10
    SQLALCHEMY_MAX_OVERFLOW=20
    SQLALCHEMY_POOL_RECYCLE=1800
    SQLALCHEMY_ENGINE_OPTIONS={"pool_pre_ping": True}

    JWT_ALGORITHM="RS256"
    JWT_ACCESS_TOKEN_EXPIRES=expired
    JWT_DECODE_ALGORITHMS=["RS256"]
    JWT_PRIVATE_KEY=private_key
    JWT_PUBLIC_KEY=public_key
    JWT_REFRESH_TOKEN_EXPIRES=expired
    JWT_SECRET_KEY=os.getenv("SECRET_KEY", os.urandom(16))
    JWT_TOKEN_LOCATION = "headers"

class LocalConfig(Config):
    ENV="local"
    DEBUG=True
    JWT_COOKIE_SECURE=False
    PREFERRED_URL_SCHEME="http"
    SESSION_COOKIE_SECURE=False
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:postgres@10.6.226.232:5432/digiloan_pentest"

class DevelopmentConfig(Config):
    ENV="development"
    DEBUG=True
    JWT_COOKIE_SECURE=True
    PREFERRED_URL_SCHEME="https"
    SESSION_COOKIE_SECURE=True
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:postgres@10.6.226.232:5432/digiloan_pentest"

class ProductionConfig(Config):
    ENV="production"
    DEBUG=False
    JWT_COOKIE_SECURE=True
    PREFERRED_URL_SCHEME="https"
    SESSION_COOKIE_SECURE=True
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:postgres@10.6.226.232:5432/digiloan_pentest"

config_environment = dict(
    local=LocalConfig,
    development=DevelopmentConfig,
    production=ProductionConfig,
)

class Settings:
    # app
    app_debug: bool
    app_env: str
    app_name: str = "App Service"
    app_version: str = "1.0.0"
    app_page_size: int = 15

    # app utility
    page_size: int = 15
    use_csrf_token: bool = False
    use_https: bool = False
    use_session: bool = False

    # server
    host: str = "127.0.0.1"
    port: int = 8000

    # cors
    cors: dict = {
        "allowed_headers": ["*"],
        "allowed_methods": ["*"],
        "allowed_origins": ["*"],
        "use_credentials": False,
    }

    # logging
    log_backtrace: bool = True
    logging_compress: str
    log_diagnose: bool = True
    log_enqueue: bool = True
    logging_rotation: str
    log_serialize: bool = False

    # mail
    mail_mailer: Optional[str]
    mail_host: Optional[str]
    mail_port: int
    mail_username: Optional[str]
    mail_password: Optional[str]
    mail_encryption: Optional[str]
    mail_from_address: Optional[str]
    mail_from_name: Optional[str]
    mail_ssl: bool = False
    mail_tls: bool = False
    mail_credentials: bool = False
    mail_validate_cert: bool = False
    mail_template: str = "templates/mails"

    # trusted host
    trusted_hosts: list = ["*"]

    # session
    session_key: str = "Vbf5x55mZwrpHjpkq38kblLiDTsIHy"
    session_cookie: str = f"session_{stringcase.snakecase(app_name).lower()}"
    session_ttl: int
    session_same_site: str = "lax"
    session_http_only: bool = False

    # csrf
    csrf_key: str = session_key
    csrf_name: str = f"csrf_{stringcase.snakecase(app_name).lower()}"
    csrf_secure: bool = use_https
    csrf_same_site: str = session_same_site
    csrf_header_name: str = "x-csrf-token"

    # csrf
    api_internal_host: str = "http://127.0.0.1:8000/api/"

    class Config:
        env_file: str = ".env"