from django.core.wsgi import get_wsgi_application
from vercel_wsgi import handle

app = get_wsgi_application()
handler = handle(app)
