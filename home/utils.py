from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

#
#def render_to_pdf(template_src, context_dict={}):
#    template = get_template(template_src)
#    html  = template.render(context_dict)
#    result = BytesIO()
#    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#    if not pdf.err:
#        return HttpResponse(result.getvalue(), content_type='application/pdf')
#    return None





from IDservice import settings



def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL
    mUrl = settings.MEDIA_URL
    mRoot = settings.MEDIA_ROOT

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))

    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

def render_to_pdf(template_source, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa

    template = get_template(template_source)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result,
                        link_callback=link_callback, encoding='UTF-8')

    if not pdf.err:
        return result.getvalue()
    return None
