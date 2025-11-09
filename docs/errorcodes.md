# Errorcodes und ihre Beschreibung

## Systemfehler (kritisch)
Dies sind Fehler, die das Programm schwer beeinträchtigen.
Falls Sie einen solchen Fehler antreffen sollten, überprüfen Sie das Programm und installieren Sie es im Zweifel neu. Ansonsten kontaktieren Sie bitte den Entwickler über:
[Github](https://github.com/hasderhi)
/
[Email](mailto:Annabeth.kisling@icloud.con)

---
### Fehlercode E000 - Unerwarteter kritischer Fehler
Dieser Fehlercode tritt dann auf, wenn ein Fehler die Software so beeinträchtigt, dass sie nicht weiterhin ausgeführt werden kann. Dies kann auf viele Ursache zurückführen. Bitte wenden Sie sich in diesem Fall an den Entwickler oder installieren Sie das Programm neu.

### Fehlercode E001 - Importfehler
Dieser Fehlercode tritt auf, wenn ein Modul nicht importiert werden kann. Dies kann bei der **nativen** Version des Programmes in Python 
(```.py```-Datei) daran liegen, dass ein Modul nicht verfügbar ist. 

Benötigte Module sind:

``` 
**Nativ mit Python 3.x**
os
sys
webbrowser
ctypes

tkinter, messagebox, filedialog

**Muss installiert werden**
PIL Image, ImageTk
```

**Falls Sie die ```.exe```-Version haben**, deutet dies auf Probleme mit dem Program selbst hin. Bitte installieren Sie das Programm neu oder kontaktieren Sie den Entwickler.

### Fehlercode E002 - Interne Datei nicht gefunden
Dieser Fehlercode tritt auf, wenn eine **interne** Datei nicht gefunden werden kann. Überprüfen Sie das Programm auf Vollständigkeit und installieren Sie es ggf. neu.

### Fehlercode E003 - Sonstiger Syntaxfehler
Dieser Fehlercode tritt auf, wenn das Programm unerwartet auf einen Fehler trifft. Falls der Fehler mehrmals auftritt, kontaktieren Sie bitte den Entwickler.

## Systemfehler (nicht kritisch)
Dies sind Fehler, die das Programm beeinträchtigen, aber es nicht am Ausführen hindern.

### Fehlercode E003 - Sonstiger Fehler
Dieser Fehlercode tritt auf, wenn das Programm unerwartet auf einen Fehler trifft. Falls der Fehler mehrmals auftritt, kontaktieren Sie bitte den Entwickler.

### Fehlercode E004 - Datei konnte nicht erstellt/bearbeitet/gelöscht/geöffnet werden
Dieser Fehlercode tritt auf, wenn das Programm beim Arbeiten mit einer Datei Probleme erkannt hat. Dies könnte viele Ursachen haben:

1. Das Programm verfügt nicht über Schreib-/Leserechte im Zielspeicherort.
2. Die Datei(en) sind korruptiert.
3. Der Speicherplatz ist voll oder falsch formattiert.
4. Das Programm ist nicht korrekt installiert.

Falls der Fehler mehrmals auftritt, kontaktieren Sie bitte den Entwickler.

### Fehlercode E005 - Sonstiger Dateienfehler
Dieser Fehlercode tritt auf, wenn das Programm im Umgang mit Dateien unerwartet auf einen Fehler trifft.

Falls der Fehler mehrmals auftritt, kontaktieren Sie bitte den Entwickler.

## Benutzer:innenfehler
Diese Fehlercodes weisen auf eine Fehlbedienung durch Benutzer:innen hin.

### Fehlercode E006 - Ungültige Eingabe
Dieser Fehlercode tritt auf, wenn Benutzer:innen ungültige Eingaben in das Programm eingeben. Überprüfen Sie Eingaben/Dateien auf ihre Richtigkeit, z.B. in der ```Kriterien-Speicherung.txt```-Datei.

### Fehlercode E007 - Sonstige Fehlbedienung
Dieser Fehlercode tritt auf, wenn Benutzer:innen das Programm falsch bedienen. Bitte überprüfen Sie die von Ihnen durchgeführte Aktion und kontaktieren bei Fragen den Entwickler.

<br>
<br>
<br>
<br>
Copyright (c) 2024 Annabeth Kisling (GitHub: hasderhi)

# tk_dev - Software with passion!