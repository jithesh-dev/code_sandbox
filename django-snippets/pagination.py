
# in Views

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    restaurants = Restaurant.objects.all()

    paginator = Paginator(restaurants, 2)
    page = request.GET.get("page")
    paged_restaurants = paginator.get_page(page)

    context = {"restaurants": paged_restaurants}
    return render(request, "restaurants/index.html", context)



# Template
"""
{% if restaurants.has_other_pages %}
    <div class="pagination_fg">
    {% if restaurants.has_previous %}
        <a href="?page={{ restaurants.previous_page_number }}">&laquo;</a>
    {% else %}
        <p class="disabled">&laquo;</p>
    {% endif %} 

    {% for i in restaurants.paginator.page_range %} 
        {% if restaurants.number == i %}
        <a href="#" class="active">{{ i }}</a>
        {% else %}
        <a href="?page={{ i }}">{{ i }}</a>
        {% endif %} 
    {% endfor %}

    {% if restaurants.has_next %}
        <a href="?page={{ restaurants.next_page_number }}">&raquo;</a>
    {% else %}
        <p class="disabled">&raquo;</p>
    {% endif %}
    </div>
{% endif %}

"""