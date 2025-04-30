from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'experience', 'applied_on', 'status')
    list_filter = ('position', 'experience', 'applied_on', 'status')
    search_fields = ('name', 'email', 'position', 'cover_letter')
    date_hierarchy = 'applied_on'
    readonly_fields = ('applied_on',)
    
    fieldsets = (
        ('Applicant Information', {
            'fields': ('user', 'name', 'email', 'phone')
        }),
        ('Job Details', {
            'fields': ('position', 'experience')
        }),
        ('Application Materials', {
            'fields': ('resume', 'portfolio', 'cover_letter')
        }),
        ('Application Status', {
            'fields': ('status', 'admin_notes')
        }),
        ('Metadata', {
            'fields': ('applied_on', 'last_updated')
        }),
    )
    
    actions = ['mark_under_review', 'mark_interview_stage', 'mark_accepted', 'mark_rejected']
    
    def mark_under_review(self, request, queryset):
        queryset.update(status='under_review')
    mark_under_review.short_description = "Mark selected applications as Under Review"
    
    def mark_interview_stage(self, request, queryset):
        queryset.update(status='interview')
    mark_interview_stage.short_description = "Mark selected applications as Interview Stage"
    
    def mark_accepted(self, request, queryset):
        queryset.update(status='accepted')
    mark_accepted.short_description = "Mark selected applications as Accepted"
    
    def mark_rejected(self, request, queryset):
        queryset.update(status='rejected')
    mark_rejected.short_description = "Mark selected applications as Rejected"