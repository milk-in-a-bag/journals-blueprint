from . models import MemberProfile

def profile_status(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.memberprofile
            incomplete = not (profile.phone_number and profile.directorate)
            return {'incomplete_profile': incomplete}
        except MemberProfile.DoesNotExist:
            return {'incomplete_profile': True}
    return {}