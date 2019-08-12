from django.shortcuts import render
from django.http import JsonResponse
from common.code import *
from app01.models import Machine
from app01.excel import get_excel
from datetime import datetime

def test(request):
    file_path = '/home/liu/Downloads/data.xlsx'
    file_data = get_excel(file_path)
    response = CommonResponse()
    test = []
    for data in file_data:
        m_date = datetime.strptime(data[0], '%m/%d/%Y').date()

        machine = Machine(m_date=m_date,m_time=str(data[1]),traffic=data[2],diskname=data[3])
        test.append(machine)
        # machine.add_data(data[0],str(data[1]),data[2],data[3])
    Machine.objects.bulk_create(test)
    response.msg = '获取数据成功...'
    return JsonResponse(response.get)

def get_data(request):
    machines = Machine.objects.filter(diskname='pacpnac12_/dev/vdb_120GB').order_by('m_time')
    time_list = []
    traffic_list = []
    for machine in machines:
        time_list.append(str(machine.m_time))
        traffic_list.append(machine.traffic)
    return render(request,'line-simple.html',{'time_list':time_list,'traffic_list':traffic_list})

