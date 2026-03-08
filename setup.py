"""
Setup script per creare l'applicazione macOS standalone
"""
from setuptools import setup

APP = ['pdf_converter.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': [
        'docling',
        'reportlab',
        'markdown2',
        'tkinter',
        'PIL',
        'pydantic',
        'torch',
        'transformers',
    ],
    'includes': [
        'docling.document_converter',
        'reportlab.lib.pagesizes',
        'reportlab.lib.styles',
        'reportlab.platypus',
    ],
    'excludes': [
        'matplotlib',
        'scipy.spatial.cKDTree',
    ],
    'iconfile': None,
    'plist': {
        'CFBundleName': 'PDF Converter',
        'CFBundleDisplayName': 'PDF Converter con Docling',
        'CFBundleGetInfoString': 'Converte PDF estraendo e formattando i contenuti',
        'CFBundleIdentifier': 'com.pdfconverter.app',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHumanReadableCopyright': '2026',
        'NSHighResolutionCapable': True,
    }
}

setup(
    name='PDFConverter',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

# Made with Bob
