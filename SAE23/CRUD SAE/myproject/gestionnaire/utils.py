from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from xhtml2pdf import pisa
from .models import Etudiant, Note, UnitesEnseignement

def generate_transcript(request, student_id):
    try:
        student = Etudiant.objects.get(numero_etudiant=student_id)
    except Etudiant.DoesNotExist:
        return HttpResponse("L'étudiant spécifié n'existe pas.")

    notes = Note.objects.filter(etudiant=student)

    ues = UnitesEnseignement.objects.filter(note__in=notes).distinct()

    template = get_template('generate_transcript.html')
    context = {
        'student': student,
        'notes': notes,
        'ues': ues
    }
    rendered_html = template.render(context)

    pdf_file = settings.MEDIA_ROOT / 'transcript.pdf'
    with open(pdf_file, 'w+b') as f:
        pisa.CreatePDF(rendered_html, dest=f)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="transcript.pdf"'
    response.write(pdf_file.read())

    return response
