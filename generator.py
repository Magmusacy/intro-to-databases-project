import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker instance for Polish locale
faker = Faker('pl_PL')

# Generate SQL for Users
def generate_users(count):
    sql_statements = []
    for _ in range(count):
        first_name = faker.first_name()
        last_name = faker.last_name()
        address = faker.address().replace("'", "''")
        phone = faker.phone_number()
        city = faker.city()
        country = 'Polska'
        email = faker.email()
        start_date = datetime.now() - timedelta(days=5 * 365)  # 5 years ago
        end_date = datetime.now()
        created_at = faker.date_time_between(start_date=start_date, end_date=end_date)
        updated_at = faker.date_time_between(start_date=start_date, end_date=end_date)
        birth_date = faker.date_of_birth(minimum_age=18, maximum_age=65)

        sql_statements.append(f"""
        INSERT INTO Users (FirstName, LastName, Address, Phone, City, Country, Email, CreatedAt, UpdatedAt, BirthDate)
        VALUES ('{first_name}', '{last_name}', '{address}', '{phone}', '{city}', '{country}', '{email}', '{created_at}', '{updated_at}', '{birth_date}');
        """.strip())
    return sql_statements

# Generate SQL for ApprenticeshipCompany
def generate_companies(count):
    sql_statements = []
    for _ in range(count):
        company_name = faker.company().replace("'", "''")
        sql_statements.append(f"INSERT INTO ApprenticeshipCompany (CompanyName) VALUES ('{company_name}');")
    return sql_statements

# Generate SQL for Apprenticeships
def generate_apprenticeships(count):
    sql_statements = []
    for apprenticeship_id in range(1, count + 1):
        studies_id = random.randint(1, 10)
        company_id = random.randint(1, 10)
        title = faker.job().replace("'", "''")
        description = faker.text().replace("'", "''")
        sql_statements.append(f"""
        INSERT INTO Apprenticeships (ApprenticeshipID, StudiesID, Title, Description, CompanyID)
        VALUES ({apprenticeship_id}, {studies_id}, '{title}', '{description}', {company_id});
        """.strip())
    return sql_statements

# Generate SQL for Products
def generate_products(count):
    sql_statements = []
    for product_id in range(1, count + 1):
        teacher_id = random.randint(1, 100) if random.random() > 0.5 else 'NULL'
        sql_statements.append(f"INSERT INTO Products (ProductID, TeacherID) VALUES ({product_id}, {teacher_id});")
    return sql_statements

# Generate SQL for Orders
def generate_orders(count):
    sql_statements = []
    for order_id in range(1, count + 1):
        customer_id = random.randint(1, 100)
        order_date = faker.date_time_this_year()
        sql_statements.append(f"INSERT INTO Orders (OrderID, CustomerID, OrderDate) VALUES ({order_id}, {customer_id}, '{order_date}');")
    return sql_statements

# Generate SQL for OrderDetails
def generate_order_details(count):
    sql_statements = []
    for order_detail_id in range(1, count + 1):
        order_id = random.randint(1, 50)
        product_id = random.randint(1, 20)
        price = round(random.uniform(10.0, 500.0), 2)
        sql_statements.append(f"INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Price) VALUES ({order_detail_id}, {order_id}, {product_id}, {price});")
    return sql_statements

# Save SQL to a file
def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    user_sql = generate_users(5000)
    company_sql = generate_companies(0)
    apprenticeship_sql = generate_apprenticeships(0)
    product_sql = generate_products(0)
    order_sql = generate_orders(0)
    order_detail_sql = generate_order_details(0)

    all_sql = "\n".join(user_sql + company_sql + apprenticeship_sql + product_sql + order_sql + order_detail_sql)
    save_to_file('generated_data.sql', all_sql)
    print("SQL data has been generated and saved to 'generated_data.sql'.")
