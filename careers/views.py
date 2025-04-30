from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import JobApplication
from .forms import JobApplicationForm

# Keep your existing views
def careers_view(request):
    """View for the careers page"""
    return render(request, 'careers/careers.html')

def submit_application(request):
    """Handle job application submissions"""
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            
            # If user is logged in, associate the application with the user
            if request.user.is_authenticated:
                application.user = request.user
            
            application.save()
            
            if request.user.is_authenticated:
                messages.success(request, "Your application has been submitted successfully! Track it in your dashboard.")
                return redirect('careers:dashboard')
            else:
                messages.success(request, "Your application has been submitted successfully!")
                return redirect(reverse('careers:careers') + '#open-positions')
        else:
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
            
    # If not POST or form invalid, redirect back to careers page
    return redirect('careers:careers')

# Add these new views
@login_required
def dashboard(request):
    """User dashboard to view and track job applications"""
    applications = JobApplication.objects.filter(user=request.user).order_by('-applied_at')
    
    # Get application statistics
    status_counts = applications.values('status').annotate(count=Count('status'))
    status_dict = {item['status']: item['count'] for item in status_counts}
    
    context = {
        'applications': applications,
        'submitted_count': status_dict.get('submitted', 0),
        'under_review_count': status_dict.get('under_review', 0),
        'interview_count': status_dict.get('interview', 0),
        'accepted_count': status_dict.get('accepted', 0),
        'rejected_count': status_dict.get('rejected', 0),
    }
    
    return render(request, 'careers/dashboard.html', context)

@login_required
def application_detail(request, application_id):
    """View a specific application's details"""
    application = get_object_or_404(JobApplication, id=application_id, user=request.user)
    return render(request, 'careers/application_detail.html', {'application': application})