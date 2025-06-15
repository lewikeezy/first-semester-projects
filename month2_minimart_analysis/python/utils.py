import psycopg2

# Connect to PostgreSQL database
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="your_database", #replace with your database name
        user="your_username",     #replace with your username
        password="yoour_password" #replace with your password
    )

# Convert USD to EUR and apply 10% discount if price > $50
def convert_to_eur(price_usd):
    exchange_rate = 0.9
    price_usd = float(price_usd)  # Convert Decimal to float

    if price_usd > 50:
        price_usd *= 0.9  # 10% discount

    price_eur = price_usd * exchange_rate
    return round(price_eur, 2)


# Check if total is greater than $100
def is_large_order(total):
    return total > 100
