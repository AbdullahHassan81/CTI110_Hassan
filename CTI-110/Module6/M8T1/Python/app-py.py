from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import random
import requests
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///speedofcars.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    favorite_cars = db.relationship('FavoriteCar', backref='user', lazy=True)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

class FavoriteCar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)

class MaintenanceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_make = db.Column(db.String(50), nullable=False)
    car_model = db.Column(db.String(50), nullable=False)
    maintenance_type = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    cost = db.Column(db.Float, nullable=False)

# Authentication Routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            return "Username already exists", 400
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('index'))
        
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Car-Related Routes
@app.route('/')
def index():
    # Featured cars
    featured_cars = Car.query.order_by(db.func.random()).limit(6).all()
    return render_template('index.html', featured_cars=featured_cars)

@app.route('/cars')
def car_catalog():
    # Fetch cars with filtering and pagination
    category = request.args.get('category')
    page = request.args.get('page', 1, type=int)
    per_page = 12
    
    query = Car.query
    if category:
        query = query.filter_by(category=category)
    
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    cars = pagination.items
    
    return render_template('car_catalog.html', cars=cars, pagination=pagination)

@app.route('/car/<int:car_id>')
def car_details(car_id):
    car = Car.query.get_or_404(car_id)
    
    # Fetch similar cars
    similar_cars = Car.query.filter_by(make=car.make).limit(4).all()
    
    return render_template('car_details.html', car=car, similar_cars=similar_cars)

@app.route('/add_favorite/<int:car_id>', methods=['POST'])
@login_required
def add_favorite(car_id):
    car = Car.query.get_or_404(car_id)
    
    # Check if already in favorites
    existing = FavoriteCar.query.filter_by(user_id=current_user.id, car_id=car_id).first()
    if existing:
        return jsonify({"status": "already_exists"}), 400
    
    favorite = FavoriteCar(user_id=current_user.id, car_id=car_id)
    db.session.add(favorite)
    db.session.commit()
    
    return jsonify({"status": "success"}), 200

# Maintenance Routes
@app.route('/maintenance_tracker')
@login_required
def maintenance_tracker():
    records = MaintenanceRecord.query.filter_by(user_id=current_user.id).all()
    return render_template('maintenance_tracker.html', records=records)

@app.route('/add_maintenance', methods=['POST'])
@login_required
def add_maintenance():
    car_make = request.form['car_make']
    car_model = request.form['car_model']
    maintenance_type = request.form['maintenance_type']
    cost = float(request.form['cost'])
    
    record = MaintenanceRecord(
        user_id=current_user.id,
        car_make=car_make,
        car_model=car_model,
        maintenance_type=maintenance_type,
        cost=cost
    )
    db.session.add(record)
    db.session.commit()
    
    return redirect(url_for('maintenance_tracker'))

# Dealer and Community Routes
@app.route('/dealers')
def dealer_finder():
    # Mock dealer data (would typically come from an API or database)
    dealers = [
        {"name": "AutoMax Dealership", "location": "New York", "rating": 4.5},
        {"name": "CarNation", "location": "Los Angeles", "rating": 4.2},
        {"name": "Speed Motors", "location": "Chicago", "rating": 4.7}
    ]
    return render_template('dealer_finder.html', dealers=dealers)

@app.route('/community_forum')
def community_forum():
    # Mock forum posts
    forum_posts = [
        {"title": "Best Performance Mods for Mustang", "author": "CarEnthusiast", "replies": 24},
        {"title": "Electric vs Gasoline: The Debate", "author": "TechDriver", "replies": 37},
        {"title": "Beginner's Guide to Car Maintenance", "author": "MechanicMike", "replies": 15}
    ]
    return render_template('community_forum.html', posts=forum_posts)

# Helper function for car recommendation
def recommend_cars(user_preferences):
    # Advanced recommendation logic would go here
    # This is a simplified version
    recommended_cars = Car.query.filter_by(category=user_preferences).limit(4).all()
    return recommended_cars

@app.route('/recommendations')
@login_required
def car_recommendations():
    # In a real app, this would be based on user's past interactions
    recommended_cars = recommend_cars("Sports")
    return render_template('recommendations.html', cars=recommended_cars)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()
    # Seed some initial car data if not exists
    if Car.query.count() == 0:
        sample_cars = [
            Car(make="Ford", model="Mustang", year=2023, price=45000, category="Sports"),
            Car(make="Toyota", model="Camry", year=2023, price=28000, category="Sedan"),
            Car(make="Tesla", model="Model 3", year=2023, price=55000, category="Electric"),
            Car(make="Chevrolet", model="Corvette", year=2023, price=70000, category="Sports")
        ]
        db.session.bulk_save_objects(sample_cars)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
