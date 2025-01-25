import random
import datetime


def random_datetime(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    meeting_date = start_date + datetime.timedelta(days=random_days)

    hour = random.randint(8, 19)
    minute = random.choice([0, 15, 30, 45])
    return datetime.datetime(meeting_date.year, meeting_date.month, meeting_date.day, hour, minute)


def generate_webinars_procedure_calls(num_webinars):
    webinar_titles = [
        "Wprowadzenie do programowania w Pythonie",
        "Podstawy nauki o danych",
        "Algorytmy uczenia maszynowego",
        "Podstawy głębokiego uczenia",
        "Zasady projektowania baz danych",
        "Podstawy chmury obliczeniowej",
        "Podstawy cyberbezpieczeństwa",
        "Tworzenie frontendów z React",
        "Tworzenie backendów z Django",
        "Praktyki DevOps",
        "Metodologie Agile",
        "Etyka sztucznej inteligencji",
        "Tworzenie aplikacji mobilnych",
        "Strategie marketingu cyfrowego",
        "Przegląd technologii blockchain",
        "Podstawy tworzenia gier",
        "Analiza dużych zbiorów danych",
        "Koncepcje IoT",
        "Robotyka dla początkujących",
        "Przetwarzanie języka naturalnego",
        "Wizualizacja danych w Tableau",
        "Zaawansowane zapytania SQL",
        "Zarządzanie projektami w Jira",
        "Techniki testowania oprogramowania",
        "Modelowanie 3D w Blenderze",
        "Wprowadzenie do biotechnologii",
        "Komputery kwantowe",
        "Zastosowania rzeczywistości rozszerzonej",
        "Mistrzowska edycja wideo",
        "Etyczny hacking"
    ]

    procedure_calls = []
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2025, 12, 31)

    for i in range(1, num_webinars + 1):
        title = random.choice(webinar_titles)
        description = f"{title} to doskonała okazja do pogłębienia wiedzy w tej dziedzinie. Dowiesz się nowych praktycznych zastosowań i teorii."
        meeting_datetime = random_datetime(start_date, end_date)

        record_upload_date = meeting_datetime + datetime.timedelta(days=random.randint(1, 10))

        meeting_link = f"https://example.com/webinar/{i}"
        record_link = f"https://example.com/record/{i}"
        price = round(random.uniform(50.0, 150.0), 2)

        procedure_calls.append(
            f"EXEC CreateWebinar "
            f"@Title = N'{title}', "
            f"@Description = N'{description}', "
            f"@MeetingLink = N'{meeting_link}', "
            f"@RecordLink = N'{record_link}', "
            f"@MeetingDate = '{meeting_datetime.strftime('%Y-%m-%d %H:%M:00')}', "
            f"@RecordUploadDate = '{record_upload_date.strftime('%Y-%m-%d %H:%M:00')}', "
            f"@Price = {price};"
        )

    return procedure_calls


# Generowanie wywołań procedur
webinars_procedure_calls = generate_webinars_procedure_calls(30)

# Zapis do pliku
output_file = "webinars_procedure_calls.sql"
with open(output_file, "w", encoding="utf-8") as file:
    file.write("\n".join(webinars_procedure_calls))

print(f"Plik '{output_file}' został zapisany z 30 wywołaniami procedury składowanej.")
