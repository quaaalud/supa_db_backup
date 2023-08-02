# Supa DB Backup Utility

Supa DB Backup is a Python application that allows you to create backups of your PostgreSQL database. It uses the `pg_dump` utility from PostgreSQL 15 to create a backup and saves it to a specified directory.

## Requirements

- Python 3.6 or higher
- PostgreSQL 15
- `pg_dump` utility from PostgreSQL 15 installed and accessible in your system's PATH
- A `.env` file containing your database credentials

## Setup

1. Clone this repository to your local machine.
2. Navigate to the directory where you cloned the repository.
3. Create a `.env` file in the same directory as `config.py` with the following variables:

```bash
SUPA_PASSWORD=your_database_password
SUPA_ID=your_supabase_id
SUPA_PORT=your_database_port
SUPA_USER=your_database_username
```

Replace `your_database_password`, `your_supabase_id`, `your_database_port`, and `your_database_username` with your actual database credentials.

## Usage

To run the Supa DB Backup utility, navigate to the directory containing the `main.py` file and run the following command:

```bash
python main.py
```

This will create a backup of your PostgreSQL database and save it to the backups directory. The backup file will be named in the format DB_NAME-YYYY-MM-DD_HH-MM-SS.sql, where DB_NAME is the name of your database and YYYY-MM-DD_HH-MM-SS is the current date and time.

## Notes

- The `DB_NAME` variable in `config.py` is used for the name of the backup file and must be set manually.
- The `SUPA_URL` variable in `config.py` is generated from the `SUPA_ID` variable and should not be changed.
- The Supa DB Backup utility uses the `pg_dump` command from PostgreSQL 15 to create the backup. Make sure `pg_dump` from PostgreSQL 15 is installed and accessible in your system's PATH.
- The Supa DB Backup utility does not handle errors during the backup process. If an error occurs, it will be printed to the console.

