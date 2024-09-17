
set -o errexit
set -o pipefail
cmd="$@"

function postgres_ready(){
python << END
import sys
import psycopg
import environ

try:
    env = environ.Env()
    dbname = env.str('DB_NAME')
    user = env.str('DB_USER')
    password = env.str('DB_PASSWORD')
    dbhost = env.str('DB_HOST')
    conn = psycopg.connect(dbname=dbname, user=user, password=password, host=dbhost, port=5432)
except psycopg.OperationalError as e:
    print(f"Error connecting to PostgreSQL: {e}")
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1

done 

>&2 echo "Postgres is up - continuing..."
exec $cmd