from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_transcript_pdf(student, notes):
    # Créer un nouveau fichier PDF
    pdf_filename = f"transcript_{student.numero_etudiant}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Dessiner le contenu du relevé de notes
    c.setFont("Helvetica", 12)
    c.drawString(50, 700, f"Relevé de notes de {student.nom} {student.prenom}")
    c.drawString(50, 680, "Notes:")

    y = 660  # Position verticale initiale des notes

    for note in notes:
        c.drawString(70, y, f"Examen: {note.examen.titre}")
        c.drawString(70, y - 20, f"Note: {note.note}")
        c.drawString(70, y - 40, f"Appréciation: {note.appreciation}")
        y -= 60

    # Enregistrer le fichier PDF
    c.showPage()
    c.save()

    return pdf_filename