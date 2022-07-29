from rest_framework_simplejwt.tokens import RefreshToken


def trial(user):
    refresh= RefreshToken.for_user(user)
    response = {'access': str(refresh.access_token), 'refersh': str(refresh), "name": user.fullname}
    return response
