# Limpa arquivos e pastas de cache Python recursivamente no diretório atual

Write-Host "🔄 Limpando caches Python..."

# Deleta todas as pastas __pycache__
Get-ChildItem -Recurse -Directory -Force -Filter "__pycache__" | ForEach-Object {
    Remove-Item -Recurse -Force $_.FullName
    Write-Host "🗑️ Pasta removida: $($_.FullName)"
}

# Deleta todos os arquivos .pyc e .pyo
Get-ChildItem -Recurse -Force -Include *.pyc, *.pyo | ForEach-Object {
    Remove-Item -Force $_.FullName
    Write-Host "🗑️ Arquivo removido: $($_.FullName)"
}

Write-Host "`n✅ Limpeza finalizada."
