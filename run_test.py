import pytest
import webbrowser
import os

report_dir = "reports"
report_path = os.path.join(report_dir, "report.html")

# Crear carpeta si no existe
os.makedirs(report_dir, exist_ok=True)

# Ejecutar tests
pytest.main([
    "tests/",
    f"--html={report_path}",
    "--self-contained-html",
    "-v"
])

# Abrir reporte
full_path = os.path.abspath(report_path)
webbrowser.open(f"file://{full_path}")
