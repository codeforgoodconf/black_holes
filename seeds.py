from app.db import db, Galaxy
db.create_all()
galaxy = Galaxy(1.2, 1.1, "andrew", 100.1, True, True)
db.session.add(galaxy)
db.session.commit()
