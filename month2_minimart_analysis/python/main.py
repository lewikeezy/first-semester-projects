from utils import get_connection, convert_to_eur, is_large_order
from report_generator import generate_report
import json

def simulate_orders(cursor, conn):
    orders = [
        {"customer_id": 1, "product_id": 2, "quantity": 3},
        {"customer_id": 2, "product_id": 1, "quantity": 2},
        {"customer_id": 3, "product_id": 3, "quantity": 4}
    ]

    print("Simulating new orders...")

    for order in orders:
        cursor.execute("SELECT price FROM products WHERE Product_id = %s", (order["product_id"],))
        price = cursor.fetchone()[0]
        total = price * order["quantity"]

        if is_large_order(total):
            print(f"Large Order! Customer {order['customer_id']} → Total: ${total:.2f}")

        cursor.execute("""
            INSERT INTO orders (customer_id, product_id, quantity, order_date)
            VALUES (%s, %s, %s, CURRENT_DATE)
        """, (order["customer_id"], order["product_id"], order["quantity"]))

    conn.commit()

def show_prices_in_eur(cursor):
    cursor.execute("SELECT product_name, price FROM products")
    products = cursor.fetchall()

    print("\nPrices in EUR:")
    for name, price in products:
        price_eur = convert_to_eur(price)
        print(f"{name}: €{price_eur}")

def main():
    conn = get_connection()
    cursor = conn.cursor()

    simulate_orders(cursor, conn)
    show_prices_in_eur(cursor)

    print("\nGenerating report...")
    report = generate_report(cursor)

    # Print report
    print(json.dumps(report, indent=4))

    # Save to file
    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    cursor.close()
    conn.close()
    print("\n yes! Report saved as report.json")

if __name__ == "__main__":
    main()
