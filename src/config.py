from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = [int(admin) for admin in env.list('ADMINS')]
DB_URL = env.str('DB_URL')

assert BOT_TOKEN is not None, "BOT_TOKEN is not set in environment variables."
assert DB_URL is not None, "Please enter database URL in environment variables."
assert ADMINS is not None
