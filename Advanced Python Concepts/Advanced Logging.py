# 🔹 5. Advanced Logging (Multiple Handlers)

# Aksar tum chahoge logs console + file dono me jaye:

import logging

# Logger banao
logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# File Handler
file_handler = logging.FileHandler("myapp.log")
file_handler.setLevel(logging.ERROR)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Test logs
logger.info("This will print to console ✅")
logger.error("This will print to console + file ❌")


# 🔹 6. Real-Life Use

# API requests success/failure track karna
# Errors file me log karna (debugging ke liye)
# Background jobs ka status track karna

# ⚡ Short me:

# print() → sirf testing ke liye
# logging → production ready