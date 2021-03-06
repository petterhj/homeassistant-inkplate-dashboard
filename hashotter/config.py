from environs import Env

env = Env()
env.read_env()

DEBUG                   = env.bool("DEBUG", False)
HA_BASE_URL             = env("HA_BASE_URL", "http://homeassistant.local:8123")
HA_DASHBOARD_URL        = env("HA_DASHBOARD_URL", "/lovelace/default_view")
HA_ACCESS_TOKEN         = env("HA_ACCESS_TOKEN")
SERVER_HOST             = env("SERVER_HOST", "0.0.0.0")
SERVER_PORT             = env.int("SERVER_PORT", 80)
SERVER_OUTPUT_PATH      = env("SERVER_OUTPUT_PATH", "/dashboard.png")
SCREENSHOT_HEIGHT       = env.int("SCREENSHOT_HEIGHT", 825) # px
SCREENSHOT_WIDTH        = env.int("SCREENSHOT_WIDTH", 1200) # px
SCREENSHOT_SCALING      = env.float("SCREENSHOT_SCALING", 1)
SCREENSHOT_TIMEOUT      = env.int("SCREENSHOT_TIMEOUT", 10000) # ms
SCREENSHOT_DELAY        = env.int("SCREENSHOT_DELAY", 15) # s
SCREENSHOT_OUTPUT_PATH  = env("SCREENSHOT_OUTPUT_PATH", "output/ha.png")
SCREENSHOT_INTERVAL     = env.int("SCREENSHOT_INTERVAL", 600) # s
