from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import LoginForm,RegistrationForm
from flask_login import login_user,logout_user,login_required
from .. import db
from flask_login import login_user
from ..email import mail_message
from .import auth

