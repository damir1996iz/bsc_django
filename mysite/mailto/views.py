from django.http import HttpResponse


def index(request):
    response = HttpResponse(status=302)
    emails = request.GET["emails"]
    subject = request.GET["subject"]
    body = request.GET["body"]
    response["Location"] = "mailto:{emails}?subject={subject}&body={body}".format(
        emails=emails,
        subject=subject,
        body=body
    )
    return response
