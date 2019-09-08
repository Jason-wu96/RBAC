from django import template
register = template.Library()


@register.inclusion_tag('menu_dispaly.html')
def menu_func(request):
    menu_permission = request.session.get("menu_permission")
    return {"menu_permission":menu_permission}
