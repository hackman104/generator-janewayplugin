from utils import models, setting_handler
from plugins.<%= pathName %> import plugin_settings # fix so that looks at current directory name

from django.shortcuts import render

def inject_<%= shortName %>(context):
    request = context.get('request')
    plugin = models.Plugin.objects.get(name=plugin_settings.SHORT_NAME)
    enabled = setting_handler.get_plugin_setting(plugin, '<%= shortName %>_enabled', request.journal)

    if not enabled.value:
        return ''

    return render(request, '<%= shortName %>/inject.html')