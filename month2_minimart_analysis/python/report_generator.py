def generate_report(cursor):
    # Total quantity of products sold
    cursor.execute("SELECT SUM(quantity) FROM orders")
    result = cursor.fetchone()
    total_sold = result[0] if result[0] is not None else 0

    # Total number of orders
    cursor.execute("SELECT COUNT(*) FROM orders")
    total_orders = cursor.fetchone()[0]

    # Most popular product
    cursor.execute("""
        SELECT p.product_name, SUM(o.quantity) as total_sold
        FROM orders o
        JOIN products p ON o.product_id = p.Product_id
        GROUP BY p.product_name
        ORDER BY total_sold DESC
        LIMIT 1
    """)
    popular_product = cursor.fetchone()
    if popular_product:
        popular_name = popular_product[0]
        popular_total = popular_product[1]
    else:
        popular_name = "N/A"
        popular_total = 0

    return {
        "total_products_sold": total_sold,
        "total_orders": total_orders,
        "top_product": {
            "name": popular_name,
            "units_sold": popular_total
        }
    }
