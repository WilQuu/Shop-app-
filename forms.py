from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField, IntegerField

from wtforms.validators import DataRequired


# Creating Login Form contains email and password
class LoginForm(Form):
    username = StringField("Username", validators=[validators.Length(min=7, max=50),
                                                validators.DataRequired(message="Please Fill This Field")])

    password = PasswordField("Password", validators=[validators.DataRequired(message="Please Fill This Field")])


# Creating Registration Form contains username, name, email, password and confirm password.

class RegisterForm(Form):
    username = StringField("Username", validators=[validators.Length(min=3, max=50),
                                                   validators.DataRequired(message="Please Fill This Field")])

    email = StringField("Email", validators=[validators.Email(message="Please enter a valid email address")])

    password = PasswordField("Password", validators=[

        validators.DataRequired(message="Please Fill This Field"),

    ])

class PasswordForm(Form):
    password = PasswordField("Password", validators=[

        validators.DataRequired(message="Please Fill This Field"),

    ])

class UsernameForm(Form):
    username = StringField("Username", validators=[validators.Length(min=3, max=50),
                                                   validators.DataRequired(message="Please Fill This Field")])