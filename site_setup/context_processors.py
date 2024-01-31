from site_setup.models import SiteConfig

def site_setup(request):
    setup = SiteConfig.objects.order_by('-id').first()

    return {
        'site_setup': setup,
    }