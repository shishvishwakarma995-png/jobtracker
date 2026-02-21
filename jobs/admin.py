from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):

    # Columns shown in the admin list view
    list_display = ['company', 'role', 'status', 'applied_date', 'user']

    # Sidebar filters
    list_filter = ['status', 'applied_date']

    # Search bar — searches these fields
    search_fields = ['company', 'role', 'notes']

    # Read-only timestamps (auto-set, shouldn't be editable)
    readonly_fields = ['created_at', 'updated_at']