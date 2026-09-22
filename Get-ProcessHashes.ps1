#PS
function Get-ProcessHashes {
    $results = @()

    foreach ($proc in Get-Process) {
        try {
            $path = $proc.MainModule.FileName
            $hashObj = Get-FileHash -Path $path -Algorithm SHA256
            $result = [PSCustomObject]@{
                ProcessName = $proc.ProcessName
                PID         = $proc.Id
                FilePath    = $path
                SHA256Hash  = $hashObj.Hash
            }
            $results += $result
        } catch {
            continue  # Skips processes that can't be accessed
        }
    }

    $results | Export-Csv -Path "hashes.csv" -NoTypeInformation
    Write-Host "Hashes exported to hashes.csv"
}

Get-ProcessHashes
