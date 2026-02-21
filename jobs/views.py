    # Add these imports at the top of views.py
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import JobApplication
from .forms import JobApplicationForm


class DashboardView(LoginRequiredMixin, TemplateView):
    """Home page — shows summary counts for the logged-in user."""
    template_name = 'jobs/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Only count jobs belonging to the current user
        qs = JobApplication.objects.filter(user=self.request.user)
        context['total']        = qs.count()
        context['applied']      = qs.filter(status='applied').count()
        context['interviewing'] = qs.filter(status='interviewing').count()
        context['offers']       = qs.filter(status='offer').count()
        context['rejected']     = qs.filter(status='rejected').count()
        context['recent']       = qs[:5]   # last 5 applications
        return context


class JobListView(LoginRequiredMixin, ListView):
    """Shows all job applications for the logged-in user."""
    model               = JobApplication
    template_name       = 'jobs/job_list.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        # Base queryset: only this user's jobs
        qs = JobApplication.objects.filter(user=self.request.user)
        # Optional filtering by status via ?status=applied in the URL
        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass current filter back to template so we can highlight active filter
        context['current_status'] = self.request.GET.get('status', '')
        return context


class JobCreateView(LoginRequiredMixin, CreateView):
    """Form to add a new job application."""
    model         = JobApplication
    form_class    = JobApplicationForm
    template_name = 'jobs/job_form.html'
    success_url   = reverse_lazy('job-list')

    def form_valid(self, form):
        # Automatically set the user before saving
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UpdateView):
    """Form to edit an existing job application."""
    model         = JobApplication
    form_class    = JobApplicationForm
    template_name = 'jobs/job_form.html'
    success_url   = reverse_lazy('job-list')

    def get_queryset(self):
        # Ensure users can only edit their own jobs
        return JobApplication.objects.filter(user=self.request.user)


class JobDeleteView(LoginRequiredMixin, DeleteView):
    """Confirm and delete a job application."""
    model         = JobApplication
    template_name = 'jobs/job_confirm_delete.html'
    success_url   = reverse_lazy('job-list')

    def get_queryset(self):
        # Ensure users can only delete their own jobs
        return JobApplication.objects.filter(user=self.request.user)
    

# Add this view at the bottom of views.py
class RegisterView(CreateView):
    form_class    = UserCreationForm
    template_name = 'registration/register.html'
    success_url   = reverse_lazy('dashboard')

    def form_valid(self, form):
        # Log the user in automatically after registering
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)