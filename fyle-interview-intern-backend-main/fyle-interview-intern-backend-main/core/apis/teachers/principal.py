from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from .schema import TeacherSchema
from core.models.assignments import Teacher

principal_teacher_resources = Blueprint('principal_teacher_resources', __name__)


@principal_teacher_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of teachers"""
    teacher_list = Teacher.get_teachers_by_principal()
    teacher_list_dump = TeacherSchema().dump(teacher_list, many=True)
    return APIResponse.respond(data=teacher_list_dump)