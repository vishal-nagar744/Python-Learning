import logging

# Basic config set karo
logging.basicConfig(level=logging.INFO)

logging.debug("Ye DEBUG message hai (default me nahi dikhega)")
logging.info("App start ho gayi hai ✅")
logging.warning("Low disk space ⚠️")
logging.error("File not found ❌")
logging.critical("System crash 🚨")


# 🔹 3. Logging into a File

import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',  # 'w' for overwrite, 'a' for append
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.info("App started")
logging.error("Something went wrong")


# 🔹 4. Different Levels of Logging

# DEBUG → detailed info (development ke liye)
# INFO → general events (app started, user logged in)
# WARNING → something unusual but not breaking
# ERROR → kuch galat hua
# CRITICAL → app crash / serious issue