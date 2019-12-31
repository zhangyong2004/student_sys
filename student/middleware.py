import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print('---process_request---zy')
        return

    def process_view(self,request,func,*args,**kwargs):
        print('---process_view---')
        start = time.time()
        response = func(request) #调用视图合成的方法
        costed_time = time.time() - start
        print('costed_time={:.2f}s'.format(costed_time))
        return response

    def process_exception(self,request,exception):
        print('---process_exception---')
        pass

    def process_template_response(self,request,response):
        print('---process_template_response---')
        return response

    def process_response(self,request,response):
        print('---process_response---')
        return response


