from flask import Flask, request
from geopy.geocoders import Nominatim

app = Flask(__name__)
from flask import render_template


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', otto=name)


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict/')
@app.route('/')
def predict():
    amenities = {'High chair',
                 'Smartlock', 'Fireplace guards', 'Heating',
                 'Cleaning before checkout', 'Smoke detector', 'Lockbox',
                 'Refrigerator', 'Hot water', 'Dryer', 'Self Check-In',
                 'Smoking allowed', 'Stove', 'Bed linens', 'Microwave', 'Crib',
                 'Washer / Dryer', 'Air conditioning', 'Fire extinguisher',
                 'Coffee maker', 'Ethernet connection', 'Accessible-height bed',
                 'Keypad', '24-hour check-in', 'Baby monitor',
                 'Laptop friendly workspace', 'Breakfast', 'Family/kid friendly',
                 'Free parking on street', 'Doorman', 'Carbon monoxide detector',
                 'Gym', 'Firm matress', 'First aid kit', 'Baby bath',
                 'Children’s dinnerware', 'Private entrance',
                 'Dishes and silverware', 'Game console', 'Step-free access',
                 'Hair dryer', 'Lock on bedroom door', 'Shampoo', 'Window guards',
                 'Bathtub', 'Pool', 'Babysitter recommendations',
                 'Private bathroom', 'Buzzer/wireless intercom',
                 'Wireless Internet', 'Extra pillows and blankets',
                 'Elevator in building', 'Accessible-height toilet', 'Dog(s)',
                 'Pack ’n Play/travel crib', 'Outlet covers', 'Washer', 'Hot tub',
                 'Wheelchair accessible', 'Dishwasher', 'Changing table',
                 'Free parking on premises', 'Long term stays allowed',
                 'Room-darkening shades', 'Cooking basics', 'Cable TV',
                 'translation missing: en.hosting_amenity_49', 'Iron',
                 'Patio or balcony', 'Wide clearance to bed',
                 'Flat smooth pathway to front door', 'Kitchen', 'Wide doorway',
                 'Doorman Entry', 'Wide hallway clearance', 'Stair gates',
                 'Garden or backyard', 'Pets live on this property', 'Safety card',
                 'Suitable for events', 'Grab-rails for shower and toilet',
                 'Path to entrance lit at night', 'BBQ grill', 'Cat(s)',
                 'Table corner guards', 'Essentials', 'Indoor fireplace',
                 'translation missing: en.hosting_amenity_50',
                 'Private living room', 'Internet', 'Luggage dropoff allowed',
                 'Other pet(s)', 'Oven', 'TV',
                 'Wide clearance to shower and toilet', 'Beach essentials',
                 'Hangers', 'Pets allowed', 'Children’s books and toys'}
    amenities = sorted([amenity.title() for amenity in amenities if 'translation' not in amenity])

    cancellation_policy_types = sorted(['moderate', 'flexible', 'strict', 'no_refunds', 'super_strict_30',
                                        'long_term', 'super_strict_60'])
    bed_types = sorted(['Real Bed', 'Airbed', 'Futon', 'Pull-out Sofa', 'Couch'])
    property_types = sorted(['House', 'Apartment', 'Loft', 'Dorm', 'Condominium',
                             'Bed & Breakfast', 'Other', 'Townhouse', 'Guesthouse', 'Boat',
                             'Hostel', 'Bungalow', 'Timeshare', 'Boutique hotel', 'Guest suite',
                             'Tent', 'In-law', 'Serviced apartment', 'Villa', 'Cabin',
                             'Earth House', 'Cave', 'Castle', 'Lighthouse', 'Hut',
                             'Vacation home', 'Chalet', 'Camper/RV', 'Treehouse', 'Island',
                             'Train', 'Entire Floor'])
    room_types = sorted(['Private room', 'Entire home/apt', 'Shared room'])
    return render_template('predict.html', amenities=amenities, cancellation_policy_types=cancellation_policy_types,
                           bed_types=bed_types, property_types=property_types, room_types=room_types)


@app.route("/process_form", methods=['POST'])
def process_form():
    data = {}
    data['name'] = request.form.get("name")
    data['accommodates'] = request.form.get("accommodates")  # Need to add
    data['bathrooms'] = request.form.get("bathrooms")
    data['bedrooms'] = request.form.get("bedrooms")
    data['bed_type'] = request.form.get("bed_type")
    data['beds'] = request.form.get("beds")
    data['cancellation_policy'] = request.form.get("cancellation_policy")
    data['city'] = request.form.get("city")  # Need to add
    data['instant_bookable'] = False
    data['latitude'] = str(request.form.get("latitude"))
    data['longitude'] = str(request.form.get("longitude"))
    print(data['latitude'], data['longitude'])

    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.reverse(data['latitude']+", "+data['longitude'])
    print(location)
    zipcode_str = location.address
    zipcode_str = zipcode_str[-31:-26]

    data['metropolitan'] = 0  # Need to add
    data['property_type'] = request.form.get("property_type")
    data['room_type'] = request.form.get("room_type")
    data['zipcode'] = int(zipcode_str)
    data['discount'] = request.form.get("discount")

    amenities = {'High chair',
                 'Smartlock', 'Fireplace guards', 'Heating',
                 'Cleaning before checkout', 'Smoke detector', 'Lockbox',
                 'Refrigerator', 'Hot water', 'Dryer', 'Self Check-In',
                 'Smoking allowed', 'Stove', 'Bed linens', 'Microwave', 'Crib',
                 'Washer / Dryer', 'Air conditioning', 'Fire extinguisher',
                 'Coffee maker', 'Ethernet connection', 'Accessible-height bed',
                 'Keypad', '24-hour check-in', 'Baby monitor',
                 'Laptop friendly workspace', 'Breakfast', 'Family/kid friendly',
                 'Free parking on street', 'Doorman', 'Carbon monoxide detector',
                 'Gym', 'Firm matress', 'First aid kit', 'Baby bath',
                 "Children's dinnerware", 'Private entrance',
                 'Dishes and silverware', 'Game console', 'Step-free access',
                 'Hair dryer', 'Lock on bedroom door', 'Shampoo', 'Window guards',
                 'Bathtub', 'Pool', 'Babysitter recommendations',
                 'Private bathroom', 'Buzzer/wireless intercom',
                 'Wireless Internet', 'Extra pillows and blankets',
                 'Elevator in building', 'Accessible-height toilet', 'Dog(s)',
                 "Pack 'n Play / travel crib", 'Outlet covers', 'Washer', 'Hot tub',
                 'Wheelchair accessible', 'Dishwasher',
                 'Changing table',
                 'Free parking on premises', 'Long term stays allowed',
                 'Room-darkening shades', 'Cooking basics', 'Cable TV',
                 'translation missing: en.hosting_amenity_49', 'Iron',
                 'Patio or balcony', 'Wide clearance to bed',
                 'Flat smooth pathway to front door', 'Kitchen', 'Wide doorway',
                 'Doorman Entry', 'Wide hallway clearance', 'Stair gates',
                 'Garden or backyard', 'Pets live on this property', 'Safety card',
                 'Suitable for events', 'Grab-rails for shower and toilet',
                 'Path to entrance lit at night', 'BBQ grill', 'Cat(s)',
                 'Table corner guards', 'Essentials', 'Indoor fireplace',
                 'translation missing: en.hosting_amenity_50',
                 'Private living room', 'Internet', 'Luggage dropoff allowed',
                 'Other pet(s)', 'Oven', 'TV',
                 'Wide clearance to shower and toilet', 'Beach essentials',
                 'Hangers', 'Pets allowed', "Children's books and toys"}

    amenities = sorted([amenity.title() for amenity in amenities if 'translation' not in amenity])
    amenity_str = []

    for i in range(0, len(amenities)):
        amenity_flag = request.form.get(amenities[i])
        if amenity_flag:
            amenity_str.append(amenities[i])

    data['amenities'] = amenity_str
    return data