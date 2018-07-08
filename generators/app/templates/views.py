from utils import setting_handler, models
from plugins.<%= dirName %> import forms, plugin_settings

from django.shortcuts import render

# Admin view for turning your plugin on or off. Feel free to edit
def index(request):
    '''
    Render admin page allowing users to enable or disable the plugin
    '''
    plugin = models.Plugin.objects.get(name=plugin_settings.SHORT_NAME)
    pandoc_enabled = setting_handler.get_plugin_setting(plugin, '<%= shortName %>_enabled', request.journal, create=True,
                                                        pretty='Enable <%= shortName %>', types='boolean').processed_value
    admin_form = forms.<%= shortName %>AdminForm(initial={'<%= shortName %>_enabled': <%= shortName %>_enabled})

    if request.POST:
        admin_form = forms.<%= shortName %>AdminForm(request.POST)

        if admin_form.is_valid():
            for setting_name, setting_value in admin_form.cleaned_data.items():
                setting_handler.save_plugin_setting(plugin, setting_name, setting_value, request.journal)
                messages.add_message(request, messages.SUCCESS, '{0} setting updated.'.format(setting_name))

            return redirect(reverse('<%= managerUrl %>'))

    template = "<%= dirName %>/index.html"
    context = {
        'admin_form': admin_form,
    }

    return render(request, template, context)

# declare further views here.