import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_otp_plugin.models import Device
# from django_otp.plugins.otp_totp.models import TOTPDevice


class TOTPDeviceTable(NetBoxTable):
    # assigned_object_type = columns.ContentTypeColumn(verbose_name='Object type')
    # assigned_object = tables.Column(linkify=True, orderable=False, verbose_name='Object')
    # role = tables.Column(linkify=True)
    # comments = columns.MarkdownColumn()
    # tags = columns.TagColumn(url_name='plugins:netbox_otp_plugin:devices_list')
    
    # id = tables.Column(linkify=False)
    user = tables.Column(
        verbose_name='User',
        linkify=True,
    )
    actions = columns.ActionsColumn(
        actions=()
    )

    class Meta(NetBoxTable.Meta):
        model = Device
        fields = (
            'pk',
            'id',
            'name',
            'user',
            'created_at',
            'last_used_at',
        )
        default_columns = (
            'pk',
            'name',
            'user',
            'actions',
            'last_used_at'
        )
