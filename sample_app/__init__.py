from datetime import date, datetime

from flask import Flask, render_template, flash

from flask_bs4 import Bootstrap
from flask_nav import Nav
from flask_wtf import FlaskForm

from flask_nav.elements import Navbar, View, Subgroup, Separator, Link

from wtforms import TextField, SelectField, PasswordField, SelectMultipleField
from wtforms import SubmitField, BooleanField, RadioField, FileField
from wtforms import FloatField, DecimalField, IntegerField, FormField
from wtforms import StringField, FieldList
from wtforms.fields.html5 import DateField, DateTimeField, EmailField
from wtforms.fields.html5 import DateTimeLocalField, IntegerRangeField
from wtforms.validators import DataRequired, Email, Length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

nav = Nav()

bootstrap = Bootstrap(app)


@nav.navigation()
def mynavbar():
    return Navbar(
        'Sample App',
        View('Standard', 'standard'),
        View('Horizontal', 'horizontal'),
        View('Floating', 'floating'),
        View('Quick Form', 'quick_form'),
        Subgroup(
            'Subgroup',
            View('Standard', 'standard'),
            View('Horizontal', 'horizontal'),
            View('Floating', 'floating'),
            View('Quick Form', 'quick_form'),
            Separator(),
            Link('Github', '//github.com/hfilimonescu/flask-bs4/'),
        ),
        Link('Github', '//github.com/hfilimonescu/flask-bs4/'),
    )


nav.init_app(app)


class TelephoneForm(FlaskForm):
    country_code = IntegerField(
        'Country Code',
        validators=[DataRequired()])
    area_code = IntegerField(
        'Area Code/Exchange',
        validators=[DataRequired()])
    number = StringField('Number')


class TestForm(FlaskForm):
    name = TextField(
        'Your name',
        validators=[Length(3, 5)],
        render_kw={'autofocus': 'autofocus'})
    password = PasswordField(
        description='Your favorite password',
        validators=[])
    email = EmailField('Your email address')
    mobile_phone = FormField(TelephoneForm)
    flist = FieldList(StringField('FieldList Name'),
                      min_entries=2, label='Authors')
    remember = BooleanField(
        'Check me out',
        validators=[],
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
            Mauris ultricies libero lacus, eu ornare ex imperdiet quis.Sed non \
            aliquet magna.Praesent gravida odio id massa condimentum, quis \
            imperdiet nunc luctus.')
    ranger = IntegerRangeField(
        'The Lone Ranger',
        default=3,
        render_kw={
            'min': 0,
            'max': 6,
            'step': 1,
            'class': 'form-range',
        })
    a_float = FloatField('A floating point number')
    a_decimal = DecimalField(
        places=2,
        rounding='ROUND_HALF_UP',
        validators=[])
    a_integer = IntegerField('An integer')
    sample_file = FileField(
        'Your favorite file',
        description='A file you would like to upload.')
    radio = RadioField(
        'Radio Gaga',
        choices=[('ch_01', 'Choice 01'),
                 ('ch_02', 'Choice 02'),
                 ('ch_03', 'Choice 03')],
        default='ch_02',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
            Mauris ultricies libero lacus, eu ornare ex imperdiet quis.Sed \
            non aliquet magna.Praesent gravida odio id massa condimentum, \
            quis imperdiet nunc luctus.')
    select = SelectField(
        'Person',
        choices=[('ch_01', 'Choice 01'),
                 ('ch_02', 'Choice 02'),
                 ('ch_03', 'Choice 03')],
        default='ch_03',
        validators=[DataRequired()])
    select_multi = SelectMultipleField(
        'Persons',
        choices=[('ch_01', 'Choice 01'),
                 ('ch_02', 'Choice 02'),
                 ('ch_03', 'Choice 03')],
        default=['ch_01', 'ch_03'],
        validators=[DataRequired()])
    birthday = DateField('Your birthday', default=date.today)
    date_time = DateTimeField('DateTime', default=datetime.now)
    date_time_local = DateTimeLocalField(
        'DateTimeLocal',
        format='%Y-%m-%dT%H:%M',
        default=datetime.now)
    submit = SubmitField('Submit Form')


@app.route("/", methods=['GET', 'POST'])
def standard():
    form = TestForm()

    if form.validate_on_submit():
        flash('Message')

    return render_template('standard.html.j2', form=form)


@app.route('/horizontal/', methods=['GET', 'POST'])
def horizontal():
    form = TestForm()

    if form.validate_on_submit():
        flash('Message')

    return render_template('horizontal.html.j2', form=form)


@app.route('/floating/', methods=['GET', 'POST'])
def floating():
    form = TestForm()

    if form.validate_on_submit():
        flash('Message')

    return render_template('floating.html.j2', form=form)


@app.route('/quick_form/', methods=['GET', 'POST'])
def quick_form():
    form = TestForm()

    if form.validate_on_submit():
        flash('Message')

    return render_template('quick_form.html.j2', form=form)
