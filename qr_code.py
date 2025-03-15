import os
import qrcode
import base64


# Alle .html-Dateien im aktuellen Verzeichnis suchen
html_files = [f for f in os.listdir() if f.endswith(".html")]

for html_file in html_files:
    with open(html_file, "r", encoding="utf-8") as file:
        html_content = file.read()
    
    # HTML-Code in Base64 umwandeln
    encoded_html = base64.b64encode(html_content.encode()).decode()
    
    # Data-URL erstellen
    data_url = f"data:text/html;charset=utf-8;base64,{encoded_html}"
    
    # QR-Code generieren
    qr = qrcode.make(data_url)
    
    # PNG-Datei speichern (gleicher Name wie HTML-Datei, aber mit .png)
    qr_filename = os.path.splitext(html_file)[0] + ".png"
    qr.save(qr_filename)
    
    print(f"QR-Code gespeichert: {qr_filename}")

print("Fertig! Alle HTML-Dateien wurden in QR-Codes umgewandelt.")





