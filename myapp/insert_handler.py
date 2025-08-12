
async def handle_start(send_msg,msg,user,sender,db):
    if msg.lower()=="hi" and user.step=="start": 
                await send_msg(sender,"hello,what is your good name sir??")
                user.step = "asked name"

async def handle_asked_name(send_msg,msg,user,sender,db):
    user.name=msg
    await send_msg(sender,f"Nice to meet you{user.name}.What is your age??")
    user.step="asked age"

async def handle_asked_age(send_msg,msg,user,sender,db):
    user.age=msg
    await send_msg(sender,f"thanks {user.name}, you are all set!! \n delete profile or update profile??")
    user.step="registered"
    if msg.lower()=="delete profile":
          user.step="delete user"
    elif msg.lower()=="update profile":
          user.step="update choice"
