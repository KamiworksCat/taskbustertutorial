from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
    )