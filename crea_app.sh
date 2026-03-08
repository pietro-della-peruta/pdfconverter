#!/bin/bash
# Script per creare l'applicazione macOS

echo "🚀 Creazione applicazione PDF Converter per macOS..."
echo ""

# Attiva l'ambiente virtuale
source venv/bin/activate

# Pulisci build precedenti
echo "🧹 Pulizia build precedenti..."
rm -rf build dist

# Crea l'applicazione
echo "📦 Creazione applicazione con py2app..."
python setup.py py2app

# Verifica se la creazione è riuscita
if [ -d "dist/pdf_converter.app" ]; then
    echo ""
    echo "✅ Applicazione creata con successo!"
    
    # Sposta l'applicazione nella cartella distribuzione
    echo "📁 Spostamento in cartella distribuzione..."
    mv dist/pdf_converter.app distribuzione/PDFConverter.app
    
    echo ""
    echo "✨ Fatto! L'applicazione è disponibile in: distribuzione/PDFConverter.app"
    echo ""
    echo "Per usarla:"
    echo "  1. Apri la cartella 'distribuzione'"
    echo "  2. Trascina PDFConverter.app nella cartella Applicazioni"
    echo "  3. Fai doppio clic per avviare"
    echo ""
else
    echo ""
    echo "❌ Errore durante la creazione dell'applicazione"
    echo "Controlla i messaggi di errore sopra"
fi

# Made with Bob
