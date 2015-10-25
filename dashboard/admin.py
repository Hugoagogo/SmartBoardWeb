from django.contrib import admin

from . import models

@admin.register(models.SmartBoard)
class SmartBoardAdmin(admin.ModelAdmin):
    list_display=('name','get_channel_count')
    
    def get_channel_count(self, obj):
        return obj.channels.count()
    get_channel_count.short_description = "Channel Count"

@admin.register(models.Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display=('name','get_board_name','channel_num','get_point_count')
    list_filter = ('board',)
    
    def get_board_name(self, obj):
        return obj.board.name
    get_board_name.short_description = "Board Name"
    
    def get_point_count(self, obj):
        return obj.points.count()
    get_point_count.short_description = "Point Count"
    
    
@admin.register(models.PowerReading)
class PowerReadingAdmin(admin.ModelAdmin):
    list_display=('get_channel_name','datetime','value')
    list_filter=('channel',)
    
    def get_channel_name(self, obj):
        return obj.channel.name
    get_channel_name.short_description = "Channel Name"
	
@admin.register(models.SwitchStatus)
class SwitchStatusAdmin(admin.ModelAdmin):
    list_display=('get_board_name','datetime','status')
    list_filter=('board',)
    
    def get_board_name(self, obj):
        return obj.board.name
    get_board_name.short_description = "Board Name"