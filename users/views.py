"""Django views module for the users app"""

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from validate_email import validate_email
from .utils import token_generator

# Create your views here.


class RegistrationView(View):
    """
        Class view used for the registration functionality
    """

    def get(self, request):
        """ Method used to GET the register page """

        return render(request, 'users/register.html')

    def post(self, request):
        """ Method used for registration """

        context = {'has_error': False}
        data = request.POST
        context['data'] = data

        email = request.POST.get('email')
        username = request.POST.get('username')
        full_name = request.POST.get('name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        checkbox = request.POST.get('checkbox')

        if not validate_email(email):
            messages.add_message(request, messages.ERROR, 'Please provide a valid email')
            context['has_error'] = True

        try:
            if User.objects.get(email=email):
                messages.add_message(request, messages.ERROR, 'Provided email is already taken')
                context['has_error'] = True
        except Exception as identifier:  # pylint: disable=broad-exception-caught, unused-variable
            pass

        try:
            if User.objects.get(username=username):
                messages.add_message(request, messages.ERROR, 'Username is taken')
                context['has_error'] = True
        except Exception as identifier:  # pylint: disable=broad-exception-caught, unused-variable
            pass

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Your password must be more than 6 characters')
            context['has_error'] = True

        if password2 != password:
            messages.add_message(request, messages.ERROR, 'Your passwords MUST match')
            context['has_error'] = True
        if not checkbox:
            messages.add_message(request, messages.ERROR, 'You have to agree with the Terms of privacy.')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'users/register.html', context, status=400)

        # If there are no errors, then we create the user
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.first_name = full_name
        user.last_name = full_name
        user.is_active = True

        user.save()

        # Creating link

        current_site = get_current_site(request)  # Get the site's domain
        email_subject = 'Activate your account'

        message = render_to_string('users/activate_profile.html',
                                   {'user': user, 'domain': current_site.domain,
                                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                    # encode user id as bytes
                                    'token': token_generator.make_token(user)
                                    # Can use it also for account activation
                                    })
        send_email = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [email])

        send_email.send()

        messages.add_message(request, messages.SUCCESS,
                             'Account successfully created! A confirmation email has been sent to you.')

        return redirect('login')

class ActivateAccountView(View):
    """Class view that is used for user account activation """

    def get(self, request, uidb64, token):
        """
            Check if the parameters are correct
            in order to successfully verify account through link
         """

        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
        except Exception as identifier:  # pylint: disable=broad-exception-caught, unused-variable
            user = None

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()

            messages.add_message(request, messages.SUCCESS,
                                 ' You successfully activated your account.')

            return redirect('login')
        return render(request, 'users/activation_failed.html', status=401)

class LoginView(View):
    """Class used for user login"""

    def get(self, request):
        """ Method used to GET the login page """

        return render(request, 'users/login.html')

    def post(self, request):
        """ Method used for user login """

        context = {'has_error': False,
                   'data': request.POST
                   }

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == '':
            messages.add_message(request, messages.ERROR, 'Email is required for user login')
            context['has_error'] = True

        if password == '':
            messages.add_message(request, messages.ERROR, 'Password is required for user login')
            context['has_error'] = True

        user = authenticate(request, username=username, password=password)

        if not user and not context['has_error']:  # Checking if authentication method has failed
            messages.add_message(request, messages.ERROR, 'Invalid login. Try to login again')
            context['has_error'] = True
        if context['has_error']:
            return render(request, 'users/login.html', status=401, context=context)

        # If there are no errors:
        login(request, user)

        return redirect('base')


class LogOutView(View):
    """Class view that is used for user logout functionality """
    def get(self, request):
        """Method for logging user out """
        logout(request)
        messages.add_message(request, messages.SUCCESS, ' You successfully logged out.')
        return redirect('base')
