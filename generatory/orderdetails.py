import random
import json

def generate_massive_sql_file(output_file="massive_orders.sql"):
    """
    Generates an SQL file with EXEC CreateNewOrder statements for each CustomerID (1-1000),
    having a random number of orders (0-10), and for each order selecting random ProductIDs (from 1 to 67)
    in the specified JSON format.

    Parameters:
    - output_file (str): The name of the SQL file to generate.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("-- Generated SQL script for massive orders\n")
            file.write("-- Copy and paste into SQL Server Management Studio to execute\n\n")

            for customer_id in range(1, 999):  # CustomerIDs from 1 to 1000
                num_products = random.randint(1, 10)

                product_ids = random.sample(range(1, 931), num_products)

                products_json = [{"ProductID": pid} for pid in product_ids]

                products_json_str = json.dumps(products_json)

                sql_command = f"EXEC CreateNewOrder @CustomerID = {customer_id}, @Products = '{products_json_str}';\n"
                file.write(sql_command)

        print(f"SQL file '{output_file}' has been successfully generated.")
    except Exception as e:
        print(f"An error occurred: {e}")

output_file = "massive_orders.sql"
generate_massive_sql_file(output_file)
