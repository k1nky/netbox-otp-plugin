import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_otp_plugin.models import Device


class TOTPDeviceTable(NetBoxTable):
    user = tables.Column(
        verbose_name='User',
        linkify=True,
    )
    name = tables.Column(
        verbose_name='Name',
        linkify=True
    )

    actions = columns.ActionsColumn(
        actions=('edit', 'delete',)
    )

    class Meta(NetBoxTable.Meta):
        model = Device
        fields = (
            'pk',
            'id',
            'name',
            'user',
            'digits',
            'created_at',
            'last_used_at',
            'actions'
        )
        default_columns = (
            'pk',
            'name',
            'user',
            'actions',
            'last_used_at',
            'default_action'
        )
