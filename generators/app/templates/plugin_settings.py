PLUGIN_NAME = '<%= pluginName %>'
DESCRIPTION = '<%= description %>'
AUTHOR = '<%= author %>'
VERSION = '<%= version %>'
SHORT_NAME = '<%= shortName %>'
MANAGER_URL = '<%= managerUrl %>'

from utils import models

def install():
    new_plugin, created = models.Plugin.objects.get_or_create(name=SHORT_NAME, version=VERSION, enabled=True)

    if created:
        print('Plugin {0} installed.'.format(PLUGIN_NAME))
    else:
        print('Plugin {0} is already installed.'.format(PLUGIN_NAME))
        
    models.PluginSetting.objects.get_or_create(name='<%= shortName %>_enabled', plugin=new_plugin, types='boolean',
                                               pretty_name='Enable <%= shortName %>', description='Enable <%= shortName %>',
                                               is_translatable=False)

def hook_registry():
    # TODO: fill this in! you will need to declare a name for the hook, the module where to find the hook defined,
    # and  the function in the module. The function name will have to match the function in hooks.py
    # ex: return {'article_footer_block': {'module': 'plugins.disqus.hooks', 'function': 'inject_disqus'}}
    return