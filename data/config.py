from environs import Env
from glQiwiApi import QiwiWrapper
# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

QIWI_TOKEN=env.str('QIWI_TOKEN')
WALLET_QIWI=env.str('WALLET_QIWI')
QIWI_PUBKEY=env.str('QIWI_PUBKEY')
QIWI_SECRET_KEY=env.str('QIWI_SECRET_KEY')

DB_USER = env.str('DB_USER')
DB_PASS = env.str('DB_PASS')
DB_HOST = env.str('DB_HOST')
DB_NAME = env.str('DB_NAME')

wallet = QiwiWrapper(secret_p2p="YOUR_SECRET_P2P_TOKEN")

ADVEGO_TOKEN = env.str('ADVEGO_TOKEN')

email = env.str('email')

POSTGRES_URI = f'postgresql://{DB_USER}:{DB_PASS}@{IP}/{DB_NAME}'