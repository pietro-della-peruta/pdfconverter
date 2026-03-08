# PDF Converter con Docling

Questo programma Python utilizza la libreria [Docling](https://www.docling.ai/) per leggere file PDF, estrarre i contenuti e salvarli in vari formati.

## Caratteristiche

- ✅ Interfaccia grafica intuitiva con tkinter
- ✅ Selezione file PDF tramite dialog
- ✅ Estrazione contenuti con Docling
- ✅ Supporto OCR per PDF scansionati
- ✅ Estrazione struttura tabelle
- ✅ Export in formato Markdown
- ✅ Export metadati in formato JSON
- ✅ Salvataggio PDF processato

## 🚀 Distribuzione per macOS

Per gli utenti macOS è disponibile una versione semplificata da distribuire:

### Installazione Rapida
1. Vai nella cartella `distribuzione`
2. Esegui: `./installa.sh`
3. Avvia l'app con doppio clic su `PDFConverter.command`

**Oppure** crea un'applicazione .app standalone:
```bash
./crea_app.sh
```

📖 Vedi [distribuzione/README_DISTRIBUZIONE.md](distribuzione/README_DISTRIBUZIONE.md) per dettagli completi.

---

## Requisiti

- Python 3.8 o superiore
- Sistema operativo: macOS, Linux, o Windows

## Installazione per Sviluppatori

1. **Crea un ambiente virtuale Python:**
   ```bash
   python3 -m venv venv
   ```

2. **Attiva l'ambiente virtuale:**
   
   Su macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
   
   Su Windows:
   ```bash
   venv\Scripts\activate
   ```

3. **Installa le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```

## Utilizzo

### Avvio del programma

```bash
python pdf_converter.py
```

### Interfaccia Grafica

1. **Seleziona il file PDF di input:**
   - Clicca sul pulsante "Sfoglia..." accanto a "File PDF di input"
   - Seleziona il file PDF che vuoi convertire

2. **Specifica il file di output:**
   - Il programma suggerisce automaticamente un nome (file_originale_converted.pdf)
   - Puoi modificarlo cliccando su "Sfoglia..." accanto a "File PDF di output"

3. **Avvia la conversione:**
   - Clicca sul pulsante "Converti PDF"
   - Monitora il progresso nella barra di avanzamento e nell'area log

4. **Risultati:**
   - Il programma crea tre file:
     - `output.pdf` - **Nuovo PDF con contenuti estratti e formattati** (non una copia dell'originale)
     - `output.md` - Contenuto estratto in formato Markdown
     - `output.json` - Metadati e struttura del documento in JSON

## Output

Il programma genera tre tipi di file:

### 1. PDF Convertito
**Importante**: Il file PDF generato contiene i contenuti estratti dal PDF originale, formattati in modo pulito e leggibile. Non è una copia del PDF originale, ma un nuovo documento creato dal testo estratto. Questo significa:
- ✅ Testo pulito e ben formattato
- ✅ Struttura gerarchica preservata (titoli, paragrafi, liste)
- ✅ Dimensione file ridotta
- ❌ Immagini e grafici non inclusi
- ❌ Formattazione originale non preservata

### 2. File Markdown (.md)
Contiene il testo estratto dal PDF in formato Markdown, inclusi:
- Titoli e sottotitoli
- Paragrafi
- Liste
- Tabelle (in formato Markdown)
- Formule matematiche (se presenti)

### 3. File JSON (.json)
Contiene tutti i metadati e la struttura del documento:
- Informazioni sul documento
- Struttura gerarchica
- Posizioni degli elementi
- Metadati delle immagini
- Struttura delle tabelle

## Funzionalità Docling

Docling offre:
- **OCR avanzato**: Riconoscimento testo da PDF scansionati
- **Estrazione tabelle**: Mantiene la struttura delle tabelle
- **Formule matematiche**: Estrae e converte formule LaTeX
- **Layout analysis**: Comprende la struttura del documento
- **Multi-formato**: Supporta PDF, DOCX, PPTX, immagini

## Risoluzione Problemi

### Il programma non si avvia
- Verifica che l'ambiente virtuale sia attivato
- Controlla che tutte le dipendenze siano installate: `pip list`

### Errore durante la conversione
- Verifica che il file PDF non sia corrotto
- Controlla che il file PDF non sia protetto da password
- Assicurati di avere spazio su disco sufficiente

### OCR non funziona
- L'OCR è abilitato di default
- Per PDF di grandi dimensioni, l'OCR può richiedere tempo

## Licenza

Questo progetto è fornito come esempio educativo.

## Crediti

- [Docling](https://www.docling.ai/) - Libreria per l'elaborazione documenti
- Python tkinter - Interfaccia grafica

## Supporto

Per problemi o domande sulla libreria Docling, visita:
- Documentazione: https://www.docling.ai/
- GitHub: https://github.com/DS4SD/docling