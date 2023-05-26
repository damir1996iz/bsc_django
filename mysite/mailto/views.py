from django.http import HttpResponse
from urllib.parse import quote


def index(request):
    response = HttpResponse(status=302)
    emails = request.GET["emails"]
    subject = request.GET["subject"]
    body = request.GET["body"]
    response["Location"] = "mailto:{emails}?subject={subject}&body={body}".format(
        emails=quote(emails, "utf-8"),
        subject=quote(subject, "utf-8"),
        body=quote(body, "utf-8")
    )
    return response
