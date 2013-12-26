from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from guidepocapp.models import Region, Place, Guide, GuideToPlace
from guidepocapp.forms import RegisterGuideForm


def index(request):
    region_list = Region.objects.order_by('id')[:10]
    template = loader.get_template('guidepocapp/index.html')
    context = RequestContext(request, {
        'region_list': region_list})

    return HttpResponse(template.render(context))

# class RegionDetailView(generic):


def detail_region(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    place_list = Place.objects.filter(region=region_id).order_by('id')
    return render(request, 'guidepocapp/region_detail.html', {'region_detail': region, 'places_list': place_list})


def detail_place(request, region_id, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_list = GuideToPlace.objects.filter(place_id=place_id)

    guide_list = []
    for guide_to_place in place_list:
        guide_list += Guide.objects.filter(id=guide_to_place.guide_id_id)

    return render(request, 'guidepocapp/place_detail.html', {'place_detail': place, 'guide_list': guide_list})


def detail_guide(request, guide_id):
    guide = get_object_or_404(Guide, pk=guide_id)
    return render(request, 'guidepocapp/guide_detail.html', {'guide_detail': guide})


def register_guide(request):
    if request.method == 'POST':
        form = RegisterGuideForm(request.POST)
        if form.is_valid():
            #todo: change this crap
            res = form.save()

            return HttpResponseRedirect(reverse('guide details', args=(res.id,))) # Redirect after POST
    else:
        form = RegisterGuideForm()

    return render(request, 'guidepocapp/register_guide.html', {'form': form})


def complete(request):
    return HttpResponse("lalala")