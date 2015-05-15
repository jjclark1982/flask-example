# When executing the 'server' package, start a server

import os
from app import app

app.run(port=int(os.environ.get('PORT') or 8000))
