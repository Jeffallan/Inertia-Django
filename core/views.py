import json
from inertia import render #, ValidationError
import inertia
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages
from django.core.paginator import EmptyPage

from django.http import QueryDict


def _get_previous_page_number(sup):
    if sup.context_data["page_obj"].has_previous():
        return sup.context_data["page_obj"].previous_page_number
    return None

def _get_next_page_number(sup):
    if sup.context_data["page_obj"].has_next():
        return sup.context_data["page_obj"].next_page_number
    return None

def _get_page_data(sup):
    return{
        "has_next": sup.context_data["page_obj"].has_next(),
        "has_previous": sup.context_data["page_obj"].has_previous(),
        "previous_number": _get_previous_page_number(sup),
        "next_number": _get_next_page_number(sup),
        "current_number": sup.context_data["page_obj"].number,
        "number_pages":  sup.context_data["page_obj"].paginator.num_pages,
        "count": sup.context_data["page_obj"].paginator.count,
        "per_page": sup.context_data["page_obj"].paginator.per_page,
        "is_paginated": sup.context_data["page_obj"].paginator.num_pages > 1
    }

class InertiaListView(ListView):
    model = None
    prop_name = None
    inertia_view = None
    paginate_by=25

    def get(self, request, *args, **kwargs):
        sup = super().get(self)
        #messages.add_message(request, messages.INFO, 'Message from list')
        return render(request,
                      self.inertia_view,
                      props={self.prop_name: sup.context_data['object_list'],
                             "page": {**_get_page_data(sup)} 
                                      
                             }
                        )
    
class InertiaDetailView(DetailView):
    model = None
    prop_name = None
    inertia_view = None
    
    def get(self, request, *args, **kwargs):
        sup = super().get(self)
        #messages.add_message(request, messages.INFO, 'message from detail')
        return render(request,
                      self.inertia_view,
                      props = {self.prop_name: sup.context_data['object'],
                               }
                     )

class InertiaUpdateOrCreateView(View):
    model = None
    prop_name = None
    inertia_view = None
    redirect_url = None
    form_class = None

    def get(self, request, *args, **kwargs):
        sup = self.model.objects.get(id=kwargs["pk"])
        return render(request,
                      self.inertia_view,
                      props = {self.prop_name: sup,
                               }
                     )
    def put(self, request, *args, **kwargs):
        if self.form_class:
            #print(request.content_params)
            #print(request.content_type)
            #print(request.body.decode("utf-8"))
            
            # This depends on content type use this for json
            try: 
                data = json.loads(request.body.decode("utf-8"))
            except json.decoder.JSONDecodeError:
                data = request.body.decode("utf-8")

            # https://stackoverflow.com/questions/73896526/how-to-save-multipart-formdata-turned-into-a-querydict-using-django-rest-frame

            print("request", request.POST)
            form_data = QueryDict("", mutable=True)
            form_data.update(data)
            frm = self.form_class(form_data)
            print("frm", frm)
            #data = request.body.decode("utf=8") #request.POST
            #print(data)
            #Use this for json
            #form = self.form_class(data=data)
            form = self.form_class(data=data)
            entry = self.model.objects.get(id=kwargs["pk"])
            #print(data)
            if form.is_valid():
                #print("form: ", form)
                for k,v in data.items():
                    setattr(entry, k, v)
                entry.save()
                messages.add_message(request, messages.INFO, {"class": "success", 
                                                              "message": f"{entry.__str__()} saved", 
                                                              "title": "Success"})
                return HttpResponseRedirect(self.redirect_url)
            #print("form invalid")
            message = json.loads(form.errors.as_json())
            #print("form: ", form)
            #print(message)
            #print(form.errors)
            #raise inertia.ValidationError(form.errors)
            for i, e in enumerate(form.errors): #message
                messages.add_message(request, messages.ERROR, {"class": "error", 
                                                               "message": message["title"][i]["message"], 
                                                               "title": "Error"})
            return HttpResponseRedirect(request.build_absolute_uri())
        else:
            raise NotImplementedError()


    def post(self, request, *args, **kwargs):
        if self.form_class:
            data = json.loads(request.body.decode("utf-8"))
            form = self.form_class(data=data)
            if form.is_valid():
                entry = form.save()
                messages.add_message(request, messages.INFO, {"class": "success", 
                                                              "message": f"{entry.__str__()} created",
                                                              "title": "Success"})
                return HttpResponseRedirect(self.redirect_url)
            message = json.loads(form.errors.as_json())
            for i, e in enumerate(form.errors):
                messages.add_message(request, messages.ERROR, {"class": "error", 
                                                               "message": message["title"][i]["message"], 
                                                               "title": "Error"})
            return HttpResponseRedirect(request.build_absolute_uri())
        else:
            raise NotImplementedError()