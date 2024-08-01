Write-Host "Verrà eseguito il seguente comando"
Write-Host "(Get-Content 'C:\Program Files\PostgreSQL\16\data\pg_hba.conf').Replace('scram-sha-256', 'trust') | Set-Content 'C:\Program Files\PostgreSQL\16\data\pg_hba.conf'"
Write-Host "Esso disabiliterà le password di postgres, eseguire solo se si è sicuri e solo se il file non è mai stato modificato e se la posizione delle cartelle è quella di default"
$editpsqlconfig = Read-Host "Va rimossa la password agli account di postgres. Scrivere 'confermo' per accettare"

if ($editpsqlconfig -eq "confermo") {
	Copy-Item 'C:\Program Files\PostgreSQL\16\data\pg_hba.conf' -Destination 'C:\Program Files\PostgreSQL\16\data\pg_hba.conf.backup'
	(Get-Content 'C:\Program Files\PostgreSQL\16\data\pg_hba.conf').Replace('scram-sha-256', 'trust') | Set-Content 'C:\Program Files\PostgreSQL\16\data\pg_hba.conf'
	Write-Host "Contenuti del file modificati"
	return 0
} else {
	Write-Host "Contenuti del file non modificati"
	return 1
}
