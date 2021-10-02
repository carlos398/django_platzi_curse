"""platzigram middleware catalog"""

#Django
from django.shortcuts import redirect



class ProfileCompletionMiddleware:
    """
    profile completion middleware
    
    Ensure every user that is interacting with the platform
    have their profile picture and biography
    
    """

    def __init__(self, get_response):
        """middleware initialization"""
        self.get_response = get_response

    
    def __call__(self, request):
        """code to be executed for each request before the view is called"""
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                return redirect('update_profile')

        response = self.get_response(request)
        return response