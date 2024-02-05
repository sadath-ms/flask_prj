from app.main import bp
from app.models import posts

@bp.route('/')
def index_page():
    return 'This is the first page...'