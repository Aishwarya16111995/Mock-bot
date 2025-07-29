import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# API Keys and credentials
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OUTLOOK_EMAIL = os.getenv("OUTLOOK_EMAIL")
OUTLOOK_PASSWORD = os.getenv("OUTLOOK_PASSWORD")
LOGIN_URL = os.getenv("LOGIN_URL", "http://localhost:5000")

# Snowflake connection settings
SNOW_USER = os.getenv("SNOW_USER", "Aishwarya1611")
SNOW_PWD = os.getenv("SNOW_PWD", "Aishwarya@12345")
SNOW_ACCOUNT = os.getenv("SNOW_ACCOUNT", "PLYIQEG-EL10623")
SNOW_WAREHOUSE = os.getenv("SNOW_WAREHOUSE", "COMPUTE_WH")
SNOW_DATABASE = os.getenv("SNOW_DATABASE", "JETKINGINTERVIEW")
SNOW_SCHEMA = os.getenv("SNOW_SCHEMA", "PUBLIC")

logging.basicConfig(level=logging.DEBUG, filename='interview_app.log', filemode='a',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", 'your-secret-key-here')
    PERMANENT_SESSION_LIFETIME = 4600
    SESSION_COOKIE_MAX_SIZE = 4093
    SESSION_TYPE = 'redis'
    SESSION_REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    SESSION_REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    SESSION_REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
    SESSION_PERMANENT = True
    SESSION_USE_SIGNER = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
    OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    
    # Snowflake Configuration
    SNOW_USER = os.getenv("SNOW_USER", "Aishwarya1611")
    SNOW_PWD = os.getenv("SNOW_PWD", "Aishwarya@12345")
    SNOW_ACCOUNT = os.getenv("SNOW_ACCOUNT", "PLYIQEG-EL10623")
    SNOW_WAREHOUSE = os.getenv("SNOW_WAREHOUSE", "COMPUTE_WH")
    SNOW_DATABASE = os.getenv("SNOW_DATABASE", "JETKINGINTERVIEW")
    SNOW_SCHEMA = os.getenv("SNOW_SCHEMA", "PUBLIC")
    
    # Interview Configuration
    MAX_FRAME_SIZE = 500
    FRAME_CAPTURE_INTERVAL = 5
    INTERVIEW_DURATION = 900
    PAUSE_THRESHOLD = 40
    ENABLE_VISUAL_ANALYSIS = True  # Set to True to enable visual analysis and feedback storage
    VISUAL_ANALYSIS_FREQUENCY = 3  # Process visual feedback every N answers (only if enabled)
    ENABLE_PERFORMANCE_MONITORING = True  # Enable performance timing logs
    VAD_SAMPLING_RATE = 16000
    VAD_FRAME_DURATION = 30
    VAD_MODE = 2
    
    # Email Configuration
    OUTLOOK_EMAIL = os.getenv("OUTLOOK_EMAIL")
    OUTLOOK_PASSWORD = os.getenv("OUTLOOK_PASSWORD")
    LOGIN_URL = os.getenv("LOGIN_URL", "http://localhost:5000")