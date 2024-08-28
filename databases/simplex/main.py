from database import create_db
from services import SpimexParser


def main():
    create_db()
    # Вводится год и месяц для сохранения данных
    parser = SpimexParser(2023, 1)
    try:
        parser.start()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
