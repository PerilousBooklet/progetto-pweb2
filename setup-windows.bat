where /q psql
IF ERRORLEVEL 1 (
    "C:\Program Files\PostgreSQL\16\bin\psql.exe" -q -f ".\sql\genera_database.sql" -d postgres -U postgres
) ELSE (
    psql -q -f ".\sql\genera_database.sql" -d postgres -U postgres
)

pause