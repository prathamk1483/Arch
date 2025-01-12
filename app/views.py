from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from docx import Document
from io import BytesIO

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

        path = f"{BASE_DIR}/templates/document.docx"

        docfile = Document(path)

        for paragraph in docfile.paragraphs:
            for key, value in data.items():
                if f"{{{{ {key} }}}}" in paragraph.text:
                    paragraph.text = paragraph.text.replace(f"{{{{ {key} }}}}", str(value))

        doc_stream = BytesIO()
        docfile.save(doc_stream)
        doc_stream.seek(0)

        # Return the Word document as an HTTP response for download
        response = HttpResponse(doc_stream, content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        response["Content-Disposition"] = f'attachment; filename="Invoice_{data["firstName"]}_{data["lastName"]}.docx"'
        return response

        return 
    
    return HttpResponse("Something went wrong")