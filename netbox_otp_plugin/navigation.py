from netbox.plugins import PluginMenu
from netbox.choices import ButtonColorChoices
from netbox.plugins import PluginMenuButton, PluginMenuItem

devices_menu_item = PluginMenuItem(
    link='plugins:netbox_otp_plugin:device_list',
    link_text='Devices',
    buttons=(
        PluginMenuButton(
            # link='plugins:netbox_otp_plugin:devices_add',
            link='plugins:netbox_otp_plugin:device_list',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.DEFAULT,
        ),
    )
)

menu = PluginMenu(
    label='TOTP Plugin',
    groups=(
        ('Devices', (devices_menu_item,)),
    ),
    icon_class='mdi mdi-router'
)
