import pymysql
import os
from dotenv import load_dotenv

# Carica le variabili dal file .env
load_dotenv()

class DatabaseWrapper:
    def __init__(self):
        # Parametri di connessione presi dall'ambiente
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.port = int(os.getenv("DB_PORT"))
        self.dbname = os.getenv("DB_NAME")
        self.connection = None

    def connect(self):
        """Stabilisce la connessione con il database MySQL."""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.dbname,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Connessione al database riuscita!")
            return self.connection
        except Exception as e:
            print(f"ErroRE di connessione: {e}")
            return None

    def init_database(self):
        """Crea la tabella deliveries se non esiste."""
        conn = self.connect()
        if not conn:
            return

        # Query SQL pura per la creazione della tabella
        query = """
        CREATE TABLE IF NOT EXISTS deliveries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tracking_code VARCHAR(100) UNIQUE NOT NULL,
            recipient VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            time_slot VARCHAR(50) NOT NULL,
            status ENUM('READY', 'OUT_FOR_DELIVERY', 'DELIVERED', 'FAILED') DEFAULT 'READY',
            priority ENUM('LOW', 'MEDIUM', 'HIGH') DEFAULT 'LOW'
        );
        """
        
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
            conn.commit()
            print("Tabella 'deliveries' inizializzata correttamente.")
        except Exception as e:
            print(f"Errore durante l'inizializzazione del DB: {e}")
        finally:
            conn.close()

# Blocco di test rapido
if __name__ == "__main__":
    db = DatabaseWrapper()
    db.init_database()