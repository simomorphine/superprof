from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class InstructionForm(FlaskForm):
    instruction = StringField('Instruction', validators=[DataRequired()])

class UploadForm(FlaskForm):
    grade = StringField('Grade', validators=[DataRequired()])
    dropdown = SelectField('Grade', choices=[('option1', 'Option 1'), 
                                               ('option2', 'Option 2'), ('option3', 'Option 3'), ('option4', 'Option 4'), ('option5', 'Option 5'), ('option6', 'Option 6')], 
                                               validators=[DataRequired()])
    files = FieldList(FileField('File', validators=[FileRequired(), 
                                                    FileAllowed(['pdf', 'doc', 'docx'], 'documents only!')]), min_entries=1)
    tags = StringField('Tags', validators=[DataRequired()])
    instructions = FieldList(FormField(InstructionForm), min_entries=1)
    submit = SubmitField('Submit')
