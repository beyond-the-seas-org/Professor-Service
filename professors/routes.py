from professors import api
from professors.apis.Add_Professor import Add_professor
from professors.apis.Add_University_Rank import Add_university_rank

Professors = api.namespace('api/professors')
Professors.add_resource(Add_professor,'/add_professor')
Professors.add_resource(Add_university_rank,'/add_university_rank')