import os
from os import getenv

from dotenv import load_dotenv
from aiohttp import ClientSession

if os.path.exists("local.env"):
    load_dotenv("local.env")
que = {}

aiohttpsession = ClientSession()

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5372076947").split()))
API_ID = int(getenv("API_ID", "13135189"))
API_HASH = getenv("API_HASH", "42186d1f48bd4d3c8233b269763b1361")
LOG_GROUP = getenv("LOG_GROUP", "-1001773996149")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")
OWNER_ID = getenv("OWNER_ID", "5372076947")
BOT_TOKEN = getenv("BOT_TOKEN", "5587599304:AAFfHH8OZtcdX8x83QuwA-JBlTnuM1t7AYI")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_USERNAME = getenv("SPOTIFY_USERNAME", "")
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://erte:wakwaw123@botmusic.kgdrx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/f710b97e74f186b847a42.jpg")
DB_URL = getenv("DATABASE_URL", "")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQCLtn1qIG49DC4xEzYfRBsNEEcLKuWjDIb4N4tZWh50ZhDzeLzQQ7x0Sgo3oLBhP168PRah-IhE1R01vITMs74qvUnoJ_SXwIDOxb3U3c9PJlX4en6JTt2WfZfq15cPUx9lDVEA-bTbMedYyC08-b83IFp0ls1nd3xph00hn3ztopvjvsjOFystEaLYTaYtNuFerrIRghjuR0uKz9Nc6CuH34Xmx2XLiwtvzvfPzaH-weUcPYOxPpXETNy6cyyuf_Y9fkdTOhVG7_ibWXCx_KoT-kDgCgwf_Xr_fNeUZpoSkK1Xd7NfLirpvHKxD2iMb7sFx9NiC0zHVaIbTRwFV2OiAAAAAUAzY5MA-PU5HfSBK6xB2sbWxAVJhNJtdbkYeGxQZr-81b-6yU4r5QGYBzcQiXAr-aglm_ZllPsWgoQKjP1mjJ68h4j3CXVakbqr36ZvSIKOKUtbI8Sj87rzrSbTFump5SdSQpnjsORxqqtsJgE8c_dxeN4aFetYBlsE-YCMZTs6jBIk0cMggM6pGys9dOV5SWtua5rBiD5QG-1mThj_tOF5xI9MozPRiq1VfK3iOPtbQVprmIpp3JelLj0qmnwV1HFoizNRAAAAAUYtUcsA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQBCHpVUdfkP7lydbY9g_fekagIleM4Pwyg_nkDf6gjz4VCvX7q26xMr0qwLdrd5v1BF_x1zyR_7MJkEoaAB7L5uOTaGhBQweFv1gkQDo5d3m2C2igU1flY7asBx0ge3S0SAnyLfG0DaqM5dPnj7NaIT_LubAAgq7RJRJ7LVk5-INtBuGJu8kIDFCGBvhbnYU4EMn-vLrIplYi434D0kWyJeXy_wjYKjvsexA9j4NZ0JAbmsl3IUDWuV4AK4YaeTIeGiLF1Ywi-YGQ1Ggsuia0MMyL-V69vqVlN3W5aq3Ts2QU7iD5EnkERUXsQu-0GJq5CfvHBKFSLXZFiKSEDvGOwWAAAAATOJJRMA")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
STRING_SESSION11 = getenv("STRING_SESSION11", "")
STRING_SESSION12 = getenv("STRING_SESSION12", "")
STRING_SESSION13 = getenv("STRING_SESSION13", "")
STRING_SESSION14 = getenv("STRING_SESSION14", "")
STRING_SESSION15 = getenv("STRING_SESSION15", "")
STRING_SESSION16 = getenv("STRING_SESSION16", "")
STRING_SESSION17 = getenv("STRING_SESSION17", "")
STRING_SESSION18 = getenv("STRING_SESSION18", "")
STRING_SESSION19 = getenv("STRING_SESSION19", "")
STRING_SESSION20 = getenv("STRING_SESSION20", "")
STRING_SESSION21 = getenv("STRING_SESSION21", "")
STRING_SESSION22 = getenv("STRING_SESSION22", "")
STRING_SESSION23 = getenv("STRING_SESSION23", "")
STRING_SESSION24 = getenv("STRING_SESSION24", "")
STRING_SESSION25 = getenv("STRING_SESSION25", "")
STRING_SESSION26 = getenv("STRING_SESSION26", "")
STRING_SESSION27 = getenv("STRING_SESSION27", "")
STRING_SESSION28 = getenv("STRING_SESSION28", "")
STRING_SESSION29 = getenv("STRING_SESSION29", "")
STRING_SESSION30 = getenv("STRING_SESSION30", "")
STRING_SESSION31 = getenv("STRING_SESSION31", "")
STRING_SESSION32 = getenv("STRING_SESSION32", "")
STRING_SESSION33 = getenv("STRING_SESSION33", "")
STRING_SESSION34 = getenv("STRING_SESSION34", "")
STRING_SESSION35 = getenv("STRING_SESSION35", "")
STRING_SESSION36 = getenv("STRING_SESSION36", "")
STRING_SESSION37 = getenv("STRING_SESSION37", "")
STRING_SESSION38 = getenv("STRING_SESSION38", "")
STRING_SESSION39 = getenv("STRING_SESSION39", "")
STRING_SESSION40 = getenv("STRING_SESSION40", "")
STRING_SESSION41 = getenv("STRING_SESSION41", "")
STRING_SESSION42 = getenv("STRING_SESSION42", "")
STRING_SESSION43 = getenv("STRING_SESSION43", "")
STRING_SESSION44 = getenv("STRING_SESSION44", "")
STRING_SESSION45 = getenv("STRING_SESSION45", "")
STRING_SESSION46 = getenv("STRING_SESSION46", "")
STRING_SESSION47 = getenv("STRING_SESSION47", "")
STRING_SESSION48 = getenv("STRING_SESSION48", "")
STRING_SESSION49 = getenv("STRING_SESSION49", "")
STRING_SESSION50 = getenv("STRING_SESSION50", "")

