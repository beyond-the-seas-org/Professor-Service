from professors import api
from professors.apis.Add_Professor import Add_professor
from professors.apis.Add_University_Rank import Add_university_rank
from professors.apis.Add_Professor_Feedback import Add_feedback
from professors.apis.Add_Professor_Publication import Add_professor_publication
from professors.apis.Add_Publication import Add_publication
from professors.apis.Add_Professor_Area_of_interest import Add_area_of_interest
from professors.apis.Add_OnGoingResearch import Add_on_going_research
from professors.apis.Add_OnGoingResearch_Professor import Add_on_going_research_professor
from professors.apis.Add_OnGoingResearch_Student import Add_on_going_research_student
from professors.apis.Add_Professor_Website import Add_website
from professors.apis.Add_Funding import Add_funding
from professors.apis.Add_Field import Add_field
from professors.apis.Get_Professor_Short_Details import Get_All_professor_short_details
from professors.apis.Get_A_Professor_Details import Get_a_professor_details
from professors.apis.Update_Professor_Image import Update_professor_image

Professors = api.namespace('api/professors')
Professors.add_resource(Add_professor,'/add_professor')
Professors.add_resource(Add_university_rank,'/add_university_rank')
Professors.add_resource(Add_feedback,'/add_feedback')
Professors.add_resource(Add_professor_publication,'/add_professor_publication')
Professors.add_resource(Add_publication,'/add_publication')
Professors.add_resource(Add_area_of_interest,'/add_area_of_interest')
Professors.add_resource(Add_on_going_research,'/add_on_going_research')
Professors.add_resource(Add_on_going_research_professor,'/add_on_going_research_professor')
Professors.add_resource(Add_on_going_research_student,'/add_on_going_research_student')
Professors.add_resource(Add_website,'/add_website')
Professors.add_resource(Add_funding,'/add_funding')
Professors.add_resource(Add_field,'/add_field')
Professors.add_resource(Get_All_professor_short_details,'/get_all_professor_short_details')
Professors.add_resource(Get_a_professor_details,'/<int:professor_id>/get_a_professor_details')
Professors.add_resource(Update_professor_image,'/<int:professor_id>/update_image')