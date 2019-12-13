from flaskblog import db
#!------------------------------------------------------------------
class User(db.Model, UserMixin):
	# id = db.Column(db.Integer, primary_key=True)  #primary key implies unique
	# # name = db.Column(db.String(50), nullable=False)
	# username = db.Column(db.String(20), unique=True, nullable=False)
	# email = db.Column(db.String(100), unique=True, nullable=False)
	# school = db.Column(db.String(50), nullable=False)
	# college = db.Column(db.String(50) )
	# company1 = db.Column(db.String(50) )
	# company2 = db.Column(db.String(50))
	# gps = db.Column(db.String(50))
	# password = db.Column(db.String(50), nullable=False)
		

	def __repr__(self):
		# return f"User('{self.username}','{self.email}')"
#!------------------------------------------------------------------

class ProductBrand(db.Model):

	id = db.Column(db.Integer, primary_key=True) 
	cd = db.Column(db.Integer, primary_key=True) 
	name = db.Column(db.String(50), nullable=False)
	description = db.Column(db.String(200), nullable=False) 
	strength = db.Column(db.String(200), nullable=False) 
	composition = db.Column(db.String(200), nullable=False) 
	mrp = db.Column(db.String(200), nullable=False)
	role_of_ingredients = db.Column(db.String(200), nullable=False)
	indication = db.Column(db.String(200), nullable=False)
	dosage = db.Column(db.String(200), nullable=False)
	usps = db.Column(db.String(200), nullable=False)
	target_customers = db.Column(db.String(200), nullable=False)
	competitors = db.Column(db.String(200), nullable=False)
	mrp = db.Column(db.String(200), nullable=False)