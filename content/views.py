from django.shortcuts import render

# Create your views here.
def projects_list(request):
  return render(request, 'content/projects_list.html')

# create, Edit, Delete... Projects
# loclaohost/content/projects
# loclaohost/content/new
# loclaohost/content/edit_id

