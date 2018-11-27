from django.http import HttpResponse

class BlockedIPSMIddleware(object):
    EXCLUDE_IPS=['127.0.0.1']
    def process_view(self,request,view_func,*view_ages,**view_kwargs):
        user_ip =request.METS['REMOTE_ADDR']
        if user_ip in BlockedIPSMIddleware.EXCLUDE_IPS:
            return HttpResponse("<h1>你被禁止访问了</h1>")