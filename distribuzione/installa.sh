#!/bin/bash
# Script di installazione per PDF Converter

echo "📦 Installazione PDF Converter"
echo "=============================="
echo ""

# Vai nella directory del progetto (parent della cartella distribuzione)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR/.."

# Verifica Python
echo "🔍 Verifica Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 non trovato!"
    echo "Installa Python 3.8 o superiore da https://www.python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python $PYTHON_VERSION trovato"
echo ""

# Crea ambiente virtuale
echo "🔧 Creazione ambiente virtuale..."
if [ -d "venv" ]; then
    echo "⚠️  Ambiente virtuale già esistente, lo rimuovo..."
    rm -rf venv
fi

python3 -m venv venv
source venv/bin/activate

# Installa dipendenze
echo ""
echo "📥 Installazione dipendenze..."
echo "Questo può richiedere alcuni minuti..."
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Installazione completata con successo!"
    echo ""
    echo "Per avviare l'applicazione:"
    echo "  - Doppio clic su: distribuzione/PDFConverter.command"
    echo "  - Oppure dal terminale: ./distribuzione/PDFConverter.command"
    echo ""
else
    echo ""
    echo "❌ Errore durante l'installazione"
    echo "Controlla i messaggi di errore sopra"
    exit 1
fi

# Made with Bob
