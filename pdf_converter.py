#!/usr/bin/env python3
"""
PDF Converter usando Docling
Questo programma legge un file PDF, estrae i contenuti usando la libreria Docling
e scrive un nuovo file PDF con i contenuti estratti.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from docling.document_converter import DocumentConverter
import threading


class PDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Converter con Docling")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        
        # Variabili
        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar()
        self.status_text = tk.StringVar(value="Pronto")
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configura l'interfaccia utente"""
        # Frame principale
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configura il ridimensionamento
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Titolo
        title_label = ttk.Label(
            main_frame, 
            text="PDF Converter con Docling", 
            font=("Helvetica", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Sezione file di input
        ttk.Label(main_frame, text="File PDF di input:", font=("Helvetica", 11)).grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        
        input_entry = ttk.Entry(main_frame, textvariable=self.input_file, width=50)
        input_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        input_button = ttk.Button(
            main_frame, 
            text="Sfoglia...", 
            command=self.select_input_file
        )
        input_button.grid(row=2, column=2, padx=(5, 0), pady=5)
        
        # Sezione file di output
        ttk.Label(main_frame, text="File PDF di output:", font=("Helvetica", 11)).grid(
            row=3, column=0, sticky=tk.W, pady=(15, 5)
        )
        
        output_entry = ttk.Entry(main_frame, textvariable=self.output_file, width=50)
        output_entry.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        output_button = ttk.Button(
            main_frame, 
            text="Sfoglia...", 
            command=self.select_output_file
        )
        output_button.grid(row=4, column=2, padx=(5, 0), pady=5)
        
        # Pulsante di conversione
        convert_button = ttk.Button(
            main_frame, 
            text="Converti PDF", 
            command=self.convert_pdf,
            style="Accent.TButton"
        )
        convert_button.grid(row=5, column=0, columnspan=3, pady=(30, 10))
        
        # Barra di progresso
        self.progress = ttk.Progressbar(
            main_frame, 
            mode='indeterminate', 
            length=400
        )
        self.progress.grid(row=6, column=0, columnspan=3, pady=10)
        
        # Label di stato
        status_label = ttk.Label(
            main_frame, 
            textvariable=self.status_text, 
            font=("Helvetica", 10),
            foreground="blue"
        )
        status_label.grid(row=7, column=0, columnspan=3, pady=10)
        
        # Area di testo per i log
        log_frame = ttk.LabelFrame(main_frame, text="Log", padding="10")
        log_frame.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        main_frame.rowconfigure(8, weight=1)
        
        self.log_text = tk.Text(log_frame, height=10, width=70, wrap=tk.WORD)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        scrollbar = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
    def log(self, message):
        """Aggiunge un messaggio al log"""
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def select_input_file(self):
        """Apre il dialogo per selezionare il file PDF di input"""
        filename = filedialog.askopenfilename(
            title="Seleziona il file PDF da convertire",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.input_file.set(filename)
            # Suggerisci automaticamente il nome del file di output
            if not self.output_file.get():
                input_path = Path(filename)
                suggested_output = input_path.parent / f"{input_path.stem}_converted.pdf"
                self.output_file.set(str(suggested_output))
            self.log(f"File di input selezionato: {filename}")
            
    def select_output_file(self):
        """Apre il dialogo per selezionare il file PDF di output"""
        filename = filedialog.asksaveasfilename(
            title="Salva il file PDF convertito come",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.output_file.set(filename)
            self.log(f"File di output selezionato: {filename}")
            
    def convert_pdf(self):
        """Esegue la conversione del PDF"""
        input_path = self.input_file.get()
        output_path = self.output_file.get()
        
        # Validazione
        if not input_path:
            messagebox.showerror("Errore", "Seleziona un file PDF di input!")
            return
            
        if not output_path:
            messagebox.showerror("Errore", "Specifica un file PDF di output!")
            return
            
        if not Path(input_path).exists():
            messagebox.showerror("Errore", "Il file di input non esiste!")
            return
            
        # Esegui la conversione in un thread separato per non bloccare l'UI
        thread = threading.Thread(target=self._do_conversion, args=(input_path, output_path))
        thread.daemon = True
        thread.start()
        
    def _create_pdf_from_markdown(self, markdown_content, output_path):
        """Crea un PDF dal contenuto Markdown usando reportlab"""
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
        from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        import re
        
        # Crea il documento PDF
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18,
        )
        
        # Prepara gli stili
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(
            name='Justify',
            parent=styles['BodyText'],
            alignment=TA_JUSTIFY,
            fontSize=11,
            leading=14
        ))
        
        # Contenitore per gli elementi del PDF
        story = []
        
        # Processa il contenuto markdown riga per riga
        lines = markdown_content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            if not line:
                # Riga vuota = spazio
                story.append(Spacer(1, 0.2*inch))
                continue
            
            # Gestisci i titoli
            if line.startswith('# '):
                text = line[2:].strip()
                para = Paragraph(text, styles['Heading1'])
                story.append(para)
                story.append(Spacer(1, 0.2*inch))
            elif line.startswith('## '):
                text = line[3:].strip()
                para = Paragraph(text, styles['Heading2'])
                story.append(para)
                story.append(Spacer(1, 0.15*inch))
            elif line.startswith('### '):
                text = line[4:].strip()
                para = Paragraph(text, styles['Heading3'])
                story.append(para)
                story.append(Spacer(1, 0.1*inch))
            elif line.startswith('#### '):
                text = line[5:].strip()
                para = Paragraph(text, styles['Heading4'])
                story.append(para)
                story.append(Spacer(1, 0.1*inch))
            elif line.startswith('- ') or line.startswith('* '):
                # Lista puntata
                text = '• ' + line[2:].strip()
                para = Paragraph(text, styles['BodyText'])
                story.append(para)
            elif re.match(r'^\d+\.\s', line):
                # Lista numerata
                para = Paragraph(line, styles['BodyText'])
                story.append(para)
            else:
                # Testo normale
                # Escape caratteri speciali per XML
                text = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                para = Paragraph(text, styles['Justify'])
                story.append(para)
        
        # Costruisci il PDF
        doc.build(story)
    
    def _do_conversion(self, input_path, output_path):
        """Esegue la conversione effettiva del PDF"""
        try:
            self.status_text.set("Conversione in corso...")
            self.progress.start()
            self.log("\n" + "="*50)
            self.log("Inizio conversione PDF")
            self.log(f"Input: {input_path}")
            self.log(f"Output: {output_path}")
            
            # Crea il converter con configurazione predefinita
            self.log("Configurazione del converter...")
            converter = DocumentConverter()
            
            # Converti il documento
            self.log("Lettura e analisi del PDF...")
            result = converter.convert(input_path)
            
            # Estrai il contenuto
            self.log("Estrazione contenuti...")
            
            # Esporta in formato Markdown (più leggibile)
            markdown_content = result.document.export_to_markdown()
            self.log(f"Contenuto estratto: {len(markdown_content)} caratteri")
            
            # Esporta anche in formato JSON per avere tutti i metadati
            json_content = result.document.export_to_dict()
            self.log(f"Metadati estratti: {len(json_content)} elementi")
            
            # Salva il contenuto estratto in un file PDF
            self.log("Creazione del nuovo PDF con i contenuti estratti...")
            
            # Salva il markdown in un file di testo
            markdown_path = Path(output_path).with_suffix('.md')
            with open(markdown_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            self.log(f"Contenuto salvato in formato Markdown: {markdown_path}")
            
            # Salva anche il JSON con tutti i metadati
            import json
            json_path = Path(output_path).with_suffix('.json')
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(json_content, f, indent=2, ensure_ascii=False)
            self.log(f"Metadati salvati in formato JSON: {json_path}")
            
            # Crea un PDF con i contenuti estratti usando reportlab
            self._create_pdf_from_markdown(markdown_content, output_path)
            self.log(f"PDF con contenuti estratti salvato: {output_path}")
            
            self.log("="*50)
            self.log("✓ Conversione completata con successo!")
            self.status_text.set("Conversione completata!")
            
            messagebox.showinfo(
                "Successo", 
                f"Conversione completata!\n\n"
                f"File PDF: {output_path}\n"
                f"File Markdown: {markdown_path}\n"
                f"File JSON: {json_path}"
            )
            
        except Exception as e:
            self.log(f"✗ ERRORE: {str(e)}")
            self.status_text.set("Errore durante la conversione")
            messagebox.showerror("Errore", f"Errore durante la conversione:\n{str(e)}")
            
        finally:
            self.progress.stop()


def main():
    """Funzione principale"""
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# Made with Bob
