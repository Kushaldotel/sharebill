import smtplib
import ssl
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework import serializers
from django.utils.html import strip_tags
#import get user model
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Ensure the password is hashed
        user.is_active = False  # Deactivate the user until email verification

        # Send verification email
        try:
            # Get the current site and build the verification link
            request = self.context.get('request')
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            verification_link = f"http://{current_site.domain}/api/verify/{uid}/{token}/"

            # Render the email template
            message = render_to_string('emails/verify_email.html', {
                'user': user,
                'verification_link': verification_link,
            })
            plain_message = strip_tags(message)
            # Use the custom send_mail function without SSL verification
            send_mail(mail_subject, plain_message, settings.EMAIL_HOST_USER, [user.email], html_message=message)

            # Save the user only if the email is sent successfully
            user.save()
        except Exception as e:
            # Log the error and raise an exception
            raise e

        return user
