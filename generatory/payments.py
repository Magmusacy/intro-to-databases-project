import random
from datetime import datetime, timedelta

ORDER_DETAIL_RANGE = (1, 5516)
NUM_RECORDS_TO_GENERATE = 20000
LOW_AMOUNT_RANGE = (5, 100)
HIGH_AMOUNT_RANGE = (800, 1000)
OUTPUT_FILENAME = "generated_payments.sql"


def generate_payments(num_records, order_detail_range, low_amount_range, high_amount_range):
    payments = []

    for _ in range(num_records):
        order_detail_id = random.randint(order_detail_range[0], order_detail_range[1])
        amount = (
            random.uniform(*low_amount_range)
            if random.random() < 0.5
            else random.uniform(*high_amount_range)
        )
        random_days = random.randint(1, 365)
        random_seconds = random.randint(0, 86399)  # Sekundy w ciągu dnia
        payment_date = datetime.now() - timedelta(days=random_days, seconds=random_seconds)
        payments.append((order_detail_id, round(amount, 2), payment_date))

    return payments



def save_to_sql_file(filename, payments):
    with open(filename, 'w') as file:
        file.write("-- Skrypt generujący dane do procedury AddPayment\n")
        file.write("-- Wygenerowano automatycznie\n\n")
        for order_detail_id, amount, payment_date in payments:
            file.write(
                f"EXEC AddPayment @OrderDetailID = {order_detail_id}, @Amount = {amount}, @PaymentDate = '{payment_date.strftime('%Y-%m-%d %H:%M:%S')}';\n"
            )
    print(f"Plik {filename} został wygenerowany.")


if __name__ == "__main__":
    payments = generate_payments(
        NUM_RECORDS_TO_GENERATE,
        ORDER_DETAIL_RANGE,
        LOW_AMOUNT_RANGE,
        HIGH_AMOUNT_RANGE,
    )
    save_to_sql_file(OUTPUT_FILENAME, payments)
