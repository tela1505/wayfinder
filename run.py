from app import create_app

app = create_app()
app.app_context().push()

# @app.before_first_request
# def create_tables():
#     db.create_all()