import os
from datetime import datetime

class Config:
    SECRET_KEY = 'your-secret-key-here'
    DATABASE_URL = 'postgresql://vapecloud_main_db_p07q_user:oPz0CigU4hEPt3GR7NOcg6aOq5wAGlxj@dpg-d6j95dcr85hc73frg5h0-a/vapecloud_main_db_p07q'
    TELEGRAM_BOT_TOKEN = '8405451677:AAHVlKIcgKnmowDNR1GX1OIeCOzmpM25Yy0'
    ADMIN_USER_ID = 5526616552  # Ваш Telegram ID
    
    # Настройки кешбека
    CASHBACK_RATE = 0.03  # 3%
    
    # Настройки сайта
    SITE_NAME = "VapeCloud"
    SITE_DESCRIPTION = "Лучший магазин вейпов и электронных сигарет"
    
    # Для Telegram Mini Apps
    BOT_USERNAME = 'VapeCloudShopBot'  # Замените на реальный username бота

    ADMIN_USERNAME = "Danil_623"