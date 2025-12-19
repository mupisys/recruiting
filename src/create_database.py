import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql
import sys
from config import DB_CONFIG


def create_database():
   
    
    DATABASE_NAME = DB_CONFIG['NAME']
    
    
    try:
        print(f"Conectando ao PostgreSQL em {DB_CONFIG['HOST']}:{DB_CONFIG['PORT']}...")
        
      
        conn = psycopg2.connect(
            dbname='postgres',
            user=DB_CONFIG['USER'],
            password=DB_CONFIG['PASSWORD'],
            host=DB_CONFIG['HOST'],
            port=DB_CONFIG['PORT']
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        cursor = conn.cursor()
        
   
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DATABASE_NAME,))
        exists = cursor.fetchone()
        
        if exists:
            print(f"Database '{DATABASE_NAME}' já existe. Nada a fazer.")
        else:

            cursor.execute(
                sql.SQL("CREATE DATABASE {}").format(
                    sql.Identifier(DATABASE_NAME)
                )
            )
            print(f"Database '{DATABASE_NAME}' criado com sucesso!")
        
        cursor.close()
        conn.close()
        

        return True
        
    except psycopg2.OperationalError as e:
        print(f"Erro de conexão: {e}")
        print("\nVerifique se:")
        print("   - O Docker está rodando: docker ps")
        print("   - O PostgreSQL está ativo: docker-compose up -d")
        print("   - As credenciais estão corretas")
        return False
        
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False


if __name__ == '__main__':
    success = create_database()
    sys.exit(0 if success else 1)