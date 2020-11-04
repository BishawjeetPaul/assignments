from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from test_app.serializers import TestSerializer
from django.views.generic import View
from test_app.models import Test
import io


class InsetData(View):
	def post(self,request):
		byte_data = request.body
		stm = io.BytesIO(byte_data)
		dict_data = JSONParser().parse(stm)
		ts = TestSerializer(data=dict_data)
		if ts.is_valid():
			ts.save()
			message = {"message":"Data is Saved"}
		else:
			message = {"errors":ts.errors}
		json_data = JSONRenderer().render(message)
		return HttpResponse(json_data, content_type="application/json")

class ViewOneData(View):
	def get(self,request,t_id):
		try:
			q_set = Test.objects.get(id=t_id)
			ts = TestSerializer(q_set)
			json_data = JSONRenderer().render(ts.data)
		except Test.DoestNotExist:
			message = {"error":"Invalid ID Number"}
			json_data = JSONRenderer().render(message)
		return HttpResponse(json_data, content_type="application/json")

class ViewallData(View):
	def get(self,request):
		q_set = Test.objects.all()
		ts = TestSerializer(q_set, many=True)
		json_data = JSONRenderer().render(ts.data)
		return HttpResponse(json_data,content_type="application/json")