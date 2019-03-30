# coding: utf-8
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, SelectField
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    email = StringField('Email address',
                        validators=[DataRequired(), Email()])
    password_hash = PasswordField('Password',
                                  validators=[DataRequired()])
    confirm = PasswordField('Confirm password',
                            validators=[DataRequired()])
    accept_tos = BooleanField('I accept the license agreement',
                              validators=[DataRequired()])
    submit = SubmitField('Create an account')


class AddMotorcycleForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    power = IntegerField('Power', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    dealer_id = SelectField('Dealer number',
                            coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add motorcycle')


class AddDealerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Add a dealership')


class SearchPriceForm(FlaskForm):
    start_price = IntegerField('Minimum price',
                               validators=[DataRequired()], default=500000)
    end_price = IntegerField('Maximum price',
                             validators=[DataRequired()], default=1000000)
    submit = SubmitField('Search')


class SearchDealerForm(FlaskForm):
    dealer_id = SelectField('Dealer number',
                            coerce=int, validators=[DataRequired()])
    submit = SubmitField('Search')
