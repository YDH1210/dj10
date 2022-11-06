from django.shortcuts import render
import googletrans

def index(request):
    b = request.GET.get("bf", "")

    context = {
        "ndict" : googletrans.LANGUAGES
    }

    if b:
        f = request.GET.get("fr", "")
        t = request.GET.get("to", "")
        trans = googletrans.Translator()
        after = trans.translate(b, src=f, dest=t)
        print(after.text)

        context.update({
            "bf" : b,
            "fr" : f,
            "to" : t,
            "af" : after.text
        })
    return render(request, 'trans/index.html', context)
# Create your views here.
