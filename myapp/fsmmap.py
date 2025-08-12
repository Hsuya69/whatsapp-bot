
#from insert_handler import handle_asked_age,handle_asked_name,handle_start
#from update_handler import handle_update_age,handle_update_choice,handle_update_name
#from delete_handler import handle_delete_user
from handler import *
'''fsmblock={
    "start":handle_start,
    "asked name":handle_asked_name,
    "asked age":handle_asked_age,
    "update choice":handle_update_choice,
    "update name":handle_update_name,
    "update age":handle_update_age,
    "delete user":handle_delete_user
}'''

fsmblock={
    "start":handle_start,
    "asked name":handle_asked_name,
    "asked age":handle_asked_age,
    "go to menu":go_to_menu,
    "show details":show_details,
    "update name":update_name,
    "update age":update_age,
    "update choice":update_choice,
    "delete user":delete_user
}

