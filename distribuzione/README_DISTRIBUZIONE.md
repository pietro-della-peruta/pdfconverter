# Distribuzione PDF Converter

## Opzione 1: Script Launcher (Consigliato)

### Installazione
1. Copia la cartella `PDFConverter` sul tuo Mac
2. Apri Terminale
3. Vai nella cartella: `cd /percorso/alla/cartella/PDFConverter`
4. Esegui: `./installa.sh`

### Utilizzo
Dopo l'installazione, puoi avviare l'applicazione in due modi:
- Doppio clic su `PDFConverter.command` nella cartella
- Dal Terminale: `./PDFConverter.command`

## Opzione 2: Applicazione macOS Standalone

Per creare un'applicazione .app standalone:

1. Apri Terminale nella cartella principale del progetto
2. Esegui: `./crea_app.sh`
3. L'applicazione sarà creata in `distribuzione/PDFConverter.app`

**Nota**: La creazione dell'app può richiedere 10-15 minuti e occupa circa 2-3 GB di spazio perché include tutte le dipendenze (PyTorch, Docling, ecc.).

## Requisiti di Sistema

- macOS 10.15 (Catalina) o superiore
- 4 GB di RAM minimo (8 GB consigliati)
- 3 GB di spazio libero su disco

## Risoluzione Problemi

### "Impossibile aprire l'applicazione perché proviene da uno sviluppatore non identificato"
1. Vai in Preferenze di Sistema > Sicurezza e Privacy
2. Clicca su "Apri comunque"

### L'applicazione non si avvia
1. Verifica di avere Python 3.8+ installato
2. Controlla che tutte le dipendenze siano installate
3. Prova a eseguire dal Terminale per vedere eventuali errori

## Supporto

Per problemi o domande, consulta il README.md principale del progetto.