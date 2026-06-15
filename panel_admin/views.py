from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def es_admin(user):
    return user.is_staff

@login_required
@user_passes_test(es_admin)
def panel_admin(request):
    return render(request, 'panel_admin/panel_admin.html')