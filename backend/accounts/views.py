from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        print("USERNAME RECEIVED:", repr(username))
        print("PASSWORD LENGTH:", len(password))

        user = authenticate(username=username, password=password)
        print("AUTH RESULT:", user)

        if user is not None:
            login(request, user)

            if user.role == "ADMIN":
                return redirect("admin_dashboard")
            elif user.role == "TEACHER":
                return redirect("teacher_dashboard")
            elif user.role == "STUDENT":
                return redirect("student_dashboard")
            elif user.role == "PARENT":
                return redirect("parent_dashboard")
            else:
                return render(request, "accounts/login.html", {
                    "error": "User role not assigned"
                })

        return render(request, "accounts/login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "accounts/login.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')


@login_required
def teacher_dashboard(request):
    return render(request, 'accounts/teacher_dashboard.html')


@login_required
def student_dashboard(request):
    return render(request, 'accounts/student_dashboard.html')


@login_required
def parent_dashboard(request):
    return render(request, 'accounts/parent_dashboard.html')
