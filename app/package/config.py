
from pydantic import  BaseSettings
from functools import lru_cache
import logging
from typing import List
import os


logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    smtp_host:          str  = os.getenv("SMTP_HOST", '')
    smtp_from:          str  = os.getenv("SMTP_FROM", '')  
    smtp_user:          str  = os.getenv("SMTP_USER", '')
    smtp_pass:          str  = os.getenv("SMTP_PASS", '')  
    smtp_tls:           bool = os.getenv("SMTP_TLS",  False)  
    accept_email:       List = os.getenv("ACCEPT_EMAIL",  [])  
    accept_title:       str  = os.getenv("ACCEPT_TITLE",  "") 
    dingding_webhook:   str  = os.getenv("DINGDING_WEBHOOK", "")
    tg_id:              int  = os.getenv("TG_ID", 0)
    tg_token:           str  = os.getenv("TG_TOKEN", "")

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def get_settings():
    logger.info("Loading config settings from the environment...")
    return Settings()


global_settings = get_settings()


# get_settings.cache_info()   # 查看缓存
# get_settings.cache_clear()  # 清楚缓存