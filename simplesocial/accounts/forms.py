from django.contrib.auth import get_user_model  # 1
from django.contrib.auth.forms import UserCreationForm  # 2


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")  # 3
        model = get_user_model()

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Customizing form (username)
            self.fields["username"].label = "Display Name"
            self.fields["username"].placeholder = "username"

            # email
            self.fields["email"].label = "Email Address"
            self.fields["email"].placeholder = "xyz@some.com"

            # password
            self.fields["password"].label = "Passcode"
