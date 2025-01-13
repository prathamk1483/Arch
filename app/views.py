from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

datavar = [
    {
        "firstName": "pratham",
        "lastName": "kubetkar",
        "age": 30,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 1000,
        "AmountPaid" : 500,
        "PlotType" : "Square"
    },
    {
        "firstName": "aniket",
        "lastName": "chavan",
        "age": 25,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 2000,
        "AmountPaid" : 1000,
        "PlotType" : "Rectangle"
    },
    {
        "firstName": "ritesh",
        "lastName": "bhagat",
        "age": 20,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 3000,
        "AmountPaid" : 1500,
        "PlotType" : "Circle"
    },
    {
        "firstName": "omkar",
        "lastName": "unde",
        "age": 35,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 4000,
        "AmountPaid" : 2000,
        "PlotType" : "Triangle"
    },
    {
        "firstName": "atharva",
        "lastName": "khatkar",
        "age": 40,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 5000,
        "AmountPaid" : 2500,
        "PlotType" : "Square"
    },
    {
        "firstName": "ashish",
        "lastName": "khatavkar",
        "age": 45,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 6000,
        "AmountPaid" : 3000,
        "PlotType" : "Rectangle"
    },
    {
        "firstName": "shantanu",
        "lastName": "bagade",
        "age": 50,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 7000,
        "AmountPaid" : 3500,
        "PlotType" : "Circle"
    },
    {
        "firstName": "akash",
        "lastName": "ganachari",
        "age": 55,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 8000,
        "AmountPaid" : 4000,
        "PlotType" : "Triangle"
    },
    {
        "firstName": "sagar",
        "lastName": "kuldharan",
        "age": 60,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 9000,
        "AmountPaid" : 4500,
        "PlotType" : "Square"
    },
    {
        "firstName": "sagar",
        "lastName": "kubetkar",
        "age": 60,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 9000,
        "AmountPaid" : 4500,
        "PlotType" : "Square"
    },
    {
        "firstName": "sagar",
        "lastName": "kulkarni",
        "age": 60,
        "address": "1234 Elm Street",
        "city": "Springfield",
        "state": "IL",
        "zipcode": "62701",
        "phone": "555-555-5555",
        "TotalBill" : 9000,
        "AmountPaid" : 4500,
        "PlotType" : "Square"
    },

]


def index(request):
    return render(request,'index.html')


def data(request):
    if request.method == 'POST':
        queryName = request.POST.get('query')
        queryName = queryName.lower()
        if queryName:
            datalist = []
            for i in datavar:
                if i['firstName'] == queryName or i['lastName'] == queryName:
                    datalist.append(i)
            return render(request, 'data.html', {'data': datalist})
    return render(request ,'data.html')


def getInvoice(request):
    if request.method == "GET":
        # Extract data from the POST request
        data = {
            "firstName": request.GET.get("firstName"),
            "lastName": request.GET.get("lastName"),
            "age": request.GET.get("age"),
            "address": request.GET.get("address"),
            "city": request.GET.get("city"),
            "state": request.GET.get("state"),
            "zipcode": request.GET.get("zipcode"),
            "phone": request.GET.get("phone"),
            "TotalBill": request.GET.get("TotalBill"),
            "AmountPaid": request.GET.get("AmountPaid"),
            "PlotType": request.GET.get("PlotType"),
        }
    
        return render(request, 'invoice.html', data)
    
    return HttpResponse("Hello Nigga")

def printInvoice(request):
    if request.method == "GET":
        # Extract data from GET request
        data = {
            "firstName": request.GET.get("firstName"),
            "lastName": request.GET.get("lastName"),
            "age": request.GET.get("age"),
            "address": request.GET.get("address"),
            "city": request.GET.get("city"),
            "state": request.GET.get("state"),
            "zipcode": request.GET.get("zipcode"),
            "phone": request.GET.get("phone"),
            "TotalBill": request.GET.get("TotalBill"),
            "AmountPaid": request.GET.get("AmountPaid"),
            "PlotType": request.GET.get("PlotType"),
            "logo_path": f"{BASE_DIR}/static/logo.png" 
        }
        data['pendingAmount'] = int(data['TotalBill']) - int(data['AmountPaid'])
        # Load the HTML template
        template = get_template(f'{BASE_DIR}/templates/invtemplate.html')
        html_content = template.render(data)

        # Generate the PDF
        pdf_stream = BytesIO()
        # Create PDF with A4 size
        pisa_status = pisa.CreatePDF(
            html_content.encode("UTF-8"), pdf_stream, encoding="UTF-8"
        )

        # Check for errors and return response
        if pisa_status.err:
            return HttpResponse("An error occurred while generating the PDF.", status=500)

        # Return the PDF as an HTTP response
        response = HttpResponse(pdf_stream.getvalue(), content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="Invoice_{data["firstName"]}_{data["lastName"]}.pdf"'
        return response

    return HttpResponse("Invalid request")
