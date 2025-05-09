
from app import db,create_app
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    
    if not User.query.filter_by(username= "admin").first():
        admin_user = User(
            username="admin",
            password= generate_password_hash("adminPassword123", method = 'pbkdf2:sha256'),
            role= "admin",
        )
        
        db.session.add(admin_user)
        db.session.commit()
        
        print("Admin created Successfully")
    else:
        print("Admin not created!")