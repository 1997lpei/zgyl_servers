from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from app.models import *
from app.get_psutil import *


# Create your views here.

# 判断登录
def auth(func):
    def inner(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if user_id:
            return func(request, *args, **kwargs)
        return HttpResponseRedirect('/login')

    return inner


# 登录
def login(request):
    if request.method == 'GET':
        request.session.flush()
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        users = User.objects.filter(userName=username, passWord=password)
        if users:
            if users.first():
                user = users.first()
                request.session['user_id'] = user.id
                return JsonResponse({"success": "登录成功!"})
        else:
            return JsonResponse({"error": "用户名和密码错误！"})


# 退出
def logout(request):
    request.session.flush()
    return render(request, 'login.html')


# 主页面
@auth
def index(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    return render(request, 'index.html', {'user': user})


def component(request):
    if request.method == 'GET':
        servers = Server.objects.all()
        return render(request, 'ADmanage.html', {'servers': servers})

    if request.method == 'POST':

        # 查询操作
        searchID = request.POST.get('searchID')
        status = request.POST.get('status')
        if searchID:
            servers = Server.objects.filter(serverID=searchID)
            return render(request, 'ADmanage.html', {'servers': servers})

        if status:
            if status == '1':
                status == bool(status)
            elif status == '0':
                status == bool(status)
            else:
                return HttpResponseRedirect('component')
            servers = Server.objects.filter(status=status)
            return render(request, 'ADmanage.html', {'servers': servers})

        # 停用启用操作
        delid = request.POST.get('delid')
        if delid:
            status = request.POST.get('uesrstatus')

            if status == '1':
                Server.objects.filter(id=delid).update(status=1)
            else:
                Server.objects.filter(id=delid).update(status=0)

        # 修改操作
        upid = request.POST.get('upid')
        if upid:
            upServerId = request.POST.get('upServerId')
            upServerNumber = request.POST.get('upServerNumber')
            upServerName = request.POST.get('upServerName')
            upServerCore = request.POST.get('upServerCore')
            if Server.objects.filter(serverID=upServerId).first() or Server.objects.filter(serialNumber=upServerNumber).first():
                return HttpResponseRedirect('component')

            if upServerId and upServerNumber and upServerName and upServerCore:
                Server.objects.filter(pk=upid).update(serverID=upServerId, serialNumber=upServerNumber,
                                                      serverName=upServerName, serverCore=upServerCore)
        return HttpResponseRedirect('component')


def change(request):
    cpu_info = get_cpu_info.delay()
    memory_info = get_memory_info.delay()
    disk_info = get_disk_info.delay()
    data = {
        'cpu_info':cpu_info,
        'memoty_info': memory_info,
        'disk_info': disk_info
    }
    return render(request, 'Serverinfo.html', data)

