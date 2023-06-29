from django.shortcuts import render, redirect

def get_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        # 在这里可以对输入的姓名进行处理或验证
        # 例如保存到数据库或验证是否符合要求

        # 重定向到 home 页面
        return redirect('home')
    else:
        # 显示姓名输入表单
        return render(request, 'get_name.html')

def home(request):
    name = request.POST.get('name')  # 获取输入的名字
    return render(request, 'home.html', {'name': name})