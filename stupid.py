from dotenv import load_dotenv
import os

load_dotenv()

print('env var:', os.getenv('CHECK'))
