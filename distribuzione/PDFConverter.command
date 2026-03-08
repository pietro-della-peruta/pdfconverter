#!/bin/bash
# PDF Converter Launcher per macOS

# Ottieni la directory dello script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Vai nella directory del progetto (parent della cartella distribuzione)
cd "$DIR/.."

# Verifica se l'ambiente virtuale esiste
if [ ! -d "venv" ]; then
    echo "❌ Ambiente virtuale non trovato!"
    echo "Esegui prima lo script di installazione: ./distribuzione/installa.sh"
    read -p "Premi INVIO per chiudere..."
    exit 1
fi

# Attiva l'ambiente virtuale
source venv/bin/activate

# Avvia l'applicazione
echo "🚀 Avvio PDF Converter..."
python pdf_converter.py

# Mantieni la finestra aperta in caso di errori
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Si è verificato un errore"
    read -p "Premi INVIO per chiudere..."
fi