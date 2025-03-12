import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

# Number of rows
num_rows = 100
num_users = 5

# Generate User Data
users = [fake.uuid4() for _ in range(num_users)]
ages = [random.randint(18, 60) for _ in range(num_users)]
genders = [random.choice(['Male', 'Female', 'Other']) for _ in range(num_users)]
locations = [fake.city() for _ in range(num_users)]
preferred_classes = [random.choice(['Economy', 'Business', 'Sleeper']) for _ in range(num_users)]
loyalty_status = [random.choice(['Bronze', 'Silver', 'Gold', 'Platinum']) for _ in range(num_users)]

user_data = pd.DataFrame({
    'User ID': users,
    'Age': ages,
    'Gender': genders,
    'Location': locations,
    'Preferred Class': preferred_classes,
    'Loyalty Status': loyalty_status
})

# Generate Booking History
train_names = ['Express', 'Superfast', 'Regional', 'Intercity', 'Night Train']
routes = [('CityA', 'CityB'), ('CityC', 'CityD'), ('CityE', 'CityF'), ('CityG', 'CityH'), ('CityI', 'CityJ')]

booking_history = pd.DataFrame({
    'User ID': [random.choice(users) for _ in range(num_rows)],
    'Train Name': [random.choice(train_names) for _ in range(num_rows)],
    'Departure': [random.choice(routes)[0] for _ in range(num_rows)],
    'Arrival': [random.choice(routes)[1] for _ in range(num_rows)],
    'Date': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_rows)],
    'Ticket Price': [round(random.uniform(10, 200), 2) for _ in range(num_rows)],
    'Seat Preference': [random.choice(['Window', 'Aisle', 'No Preference']) for _ in range(num_rows)],
})

# Generate Train Schedule
train_schedule = pd.DataFrame({
    'Train Name': [random.choice(train_names) for _ in range(num_rows)],
    'Departure Station': [random.choice(routes)[0] for _ in range(num_rows)],
    'Arrival Station': [random.choice(routes)[1] for _ in range(num_rows)],
    'Departure Time': [fake.time() for _ in range(num_rows)],
    'Arrival Time': [fake.time() for _ in range(num_rows)],
    'Duration (hrs)': [random.randint(2, 12) for _ in range(num_rows)],
    'Seat Availability': [random.randint(0, 100) for _ in range(num_rows)],
})

# Generate Pricing Data
pricing_data = pd.DataFrame({
    'Train Name': [random.choice(train_names) for _ in range(num_rows)],
    'Class': [random.choice(['Economy', 'Business', 'Sleeper']) for _ in range(num_rows)],
    'Base Price': [round(random.uniform(10, 150), 2) for _ in range(num_rows)],
    'Surge Price': [round(random.uniform(0, 50), 2) for _ in range(num_rows)],
    'Final Price': lambda df: df['Base Price'] + df['Surge Price']
}).assign(Final_Price=lambda df: df['Base Price'] + df['Surge Price'])

# Generate Contextual Data (Weather & Delays)
weather_conditions = ['Clear', 'Rainy', 'Snowy', 'Foggy', 'Windy']
delays = [random.choice([0, 5, 10, 15, 30, 45, 60]) for _ in range(num_rows)]

contextual_data = pd.DataFrame({
    'Route': [random.choice(routes) for _ in range(num_rows)],
    'Weather Condition': [random.choice(weather_conditions) for _ in range(num_rows)],
    'Delay (mins)': delays,
})

# Generate Payment Data
payment_methods = ['Credit Card', 'PayPal', 'Digital Wallet', 'Debit Card', 'Bank Transfer']
transaction_data = pd.DataFrame({
    'User ID': [random.choice(users) for _ in range(num_rows)],
    'Payment Method': [random.choice(payment_methods) for _ in range(num_rows)],
    'Amount Paid': [round(random.uniform(10, 200), 2) for _ in range(num_rows)],
    'Transaction Status': [random.choice(['Successful', 'Failed', 'Pending']) for _ in range(num_rows)],
})

# Generate Customer Feedback
ratings = [random.randint(1, 5) for _ in range(num_rows)]
feedback_data = pd.DataFrame({
    'User ID': [random.choice(users) for _ in range(num_rows)],
    'Train Name': [random.choice(train_names) for _ in range(num_rows)],
    'Rating': ratings,
    'Feedback': [fake.sentence(nb_words=10) for _ in range(num_rows)],
})

# Save DataFrames to CSV files
user_data.to_csv("user_data.csv", index=False)
booking_history.to_csv("booking_history.csv", index=False)
train_schedule.to_csv("train_schedule.csv", index=False)
pricing_data.to_csv("pricing_data.csv", index=False)
contextual_data.to_csv("contextual_data.csv", index=False)
transaction_data.to_csv("transaction_data.csv", index=False)
feedback_data.to_csv("feedback_data.csv", index=False)

# Display first few rows of each dataset
print("User Data Sample:\n", user_data.shape)
print("\nBooking History Sample:\n", booking_history.shape)
print("\nTrain Schedule Sample:\n", train_schedule.shape)
print("\nPricing Data Sample:\n", pricing_data.shape)
print("\nContextual Data Sample:\n", contextual_data.shape)
print("\nTransaction Data Sample:\n", transaction_data.shape)
print("\nCustomer Feedback Sample:\n", feedback_data.shape)
