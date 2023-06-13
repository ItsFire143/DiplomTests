from django.shortcuts import render, redirect


def getUser(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.user.username
            print(username)

        return render(request, 'timetable.html')
    else:
        print('user not authenticated')
        return redirect('home')
    return render(request, 'timetable.html')