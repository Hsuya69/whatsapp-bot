async def handle_start(send_msg,msg,user,sender,db):
    if msg.lower()=="hi" and user.step=="start": 
        await send_msg(sender,"hello, what is your good name sir??")
        user.step = "asked name"

async def handle_asked_name(send_msg,msg,user,sender,db):
    user.name=msg
    await send_msg(sender,f"Nice to meet you {user.name}. What is your age??")
    user.step="asked age"


async def handle_asked_age(send_msg,msg,user,sender,db):
    user.age=int(msg)
    await send_msg(sender,f"thanks {user.name}, you are all set!!")
    await go_to_menu(send_msg,msg,user,sender,db)

async def go_to_menu(send_msg,msg,user,sender,db):
    user.step="go to menu"
    if msg.lower() not in ["update profile","delete profile","show details"]:
        await send_msg(sender,"update profile\ndelete profile\nshow details")
        return
    if msg.lower()=="update profile":
        await update_choice(send_msg,msg,user,sender,db)
        return
    elif msg.lower()=="delete profile":
        await delete_user(send_msg,msg,user,sender,db)
        return
    elif msg.lower()=="show details":
        await show_details(send_msg,msg,user,sender,db)
        return
        
async def show_details(send_msg,msg,user,sender,db):
    name=user.name
    age=user.age
    await send_msg(sender,f"your name is {name}, and your age is {age}")
    user.step="go to menu"
    await send_msg(sender,"reply ok to go back")


async def delete_user(send_msg,msg,user,sender,db):
    try:
        await db.delete(user)
        await send_msg(sender,"deleted successfully!!")

    except Exception as e:
        await db.rollback()
        user.step="go to menu"


async def update_choice(send_msg,msg,user,sender,db):
    user.step="update choice"
    if msg.lower() not in ["name","age"]:
        await send_msg(sender,"update name or age??")
        return  
    if msg.lower()=="name":
        user.step="update name"
        await send_msg(sender,"enter your new name>")
        return
    if msg.lower()=="age":
        user.step="update age"
        await send_msg(sender,"enter your new age>")
        return
        

async def update_name(send_msg,msg,user,sender,db):
    user.name=msg
    user.step="go to menu"
    await send_msg(sender,"updated successfully \nto go back to menu \n reply 'ok'")
    return

async def update_age(send_msg,msg,user,sender,db):
    if msg.isdigit():
        user.age=int(msg)
        user.step="go to menu"
        await send_msg(sender,"updated successfully \n to go back to menu \n reply 'ok'")

    else:
        await send_msg(sender,"enter valid age in number")