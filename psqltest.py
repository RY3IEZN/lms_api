import psycopg2
import logging


def postgres_test():
    try:
        conn = psycopg2.connect(
            dbname="",
            user="",
            host="",
            port="",
            password="",
            connect_timeout=5,
        )
        conn.close()
        logging.info("Connection successful")
        return True
    except psycopg2.OperationalError as e:
        logging.error(f"OperationalError: {e}")
        return False
    except psycopg2.Error as e:
        logging.error(f"Database error: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    postgres_test()
