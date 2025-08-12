from netbox.plugins import (
    PluginMenu, PluginMenuButton, PluginMenuItem, get_plugin_config

)
from netbox.choices import ButtonColorChoices

devices_menu_item = PluginMenuItem(
    link='plugins:netbox_otp_plugin:device_list',
    link_text='Devices',
    buttons=(
        PluginMenuButton(
            link='plugins:netbox_otp_plugin:device_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.DEFAULT,
        ),
    )
)

if get_plugin_config('netbox_otp_plugin', 'top_level_menu'):
    menu = PluginMenu(
        label='TOTP Plugin',
        groups=(
            ('Devices', (devices_menu_item,)),
        ),
        icon_class='mdi mdi-router'
    )
else:
    menu_items = (
        devices_menu_item,
    )
