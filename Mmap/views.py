import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import MindMap


# 1. Login / Register
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if confirm_password:
            if password != confirm_password:
                return render(request, 'maps/login.html', {'error': 'Passwords do not match.'})
            if User.objects.filter(username=username).exists():
                return render(request, 'maps/login.html', {'error': 'That username is already taken.'})

            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('maps:select')

        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('maps:select')
            else:
                return render(request, 'maps/login.html', {'error': 'Invalid username or password.'})

    return render(request, 'maps/login.html')


# 2. Select Map
@login_required(login_url='/')
def select_view(request):
    maps = MindMap.objects.filter(owner=request.user).order_by('-updated_at')

    if request.method == 'POST':
        # "新しいマインドマップ" -> "New Mind Map"
        new_map = MindMap.objects.create(title="New Mind Map", owner=request.user)
        return redirect('maps:edit', map_id=new_map.id)

    return render(request, 'maps/select.html', {'maps': maps})


# 3. Edit Map
@login_required(login_url='/')
def edit_view(request, map_id):
    mindmap = get_object_or_404(MindMap, id=map_id, owner=request.user)

    if not mindmap.data:
        mindmap.data = [
            {
                "id": "root-init",
                "x": 300,
                "y": 200,
                "data": {"id": "node-init", "name": mindmap.title, "children": []}
            }
        ]
        mindmap.save()

    context = {
        'mindmap': mindmap,
        'map_data_json': json.dumps(mindmap.data)
    }
    return render(request, 'maps/edit.html', context)


# 4. Save Map API
@csrf_exempt
def save_map_view(request, map_id):
    if request.method == 'POST' and request.user.is_authenticated:
        mindmap = get_object_or_404(MindMap, id=map_id, owner=request.user)
        body = json.loads(request.body)

        mindmap.title = body.get('title', mindmap.title)
        mindmap.data = body.get('roots', mindmap.data)
        mindmap.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)