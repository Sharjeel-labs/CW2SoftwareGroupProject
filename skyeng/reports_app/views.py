from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML

# Create your views here.
def reports(request):
    return render(request, 'reports_app/reports.html')



def test_pdf(request):
    html_string = """
    <h1>Report Generating test</h1>
    <p>If this pdf prints, weasyprint works!</p>
    """

    pdf = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="test.pdf"'
    return response