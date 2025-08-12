
async def handle_update_choice(send_msg,msg,user,sender,db):
    if msg.lower()=="name":
        await send_msg(sender,"please enter your new name")
        user.step="update name" 
    elif msg.lower()=="age":
        await send_msg(sender,"please enter your new age")
        user.step="update age"
    else:
        await send_msg(sender,"please type either name or age!")

async def handle_update_name(send_msg,msg,user,sender,db):
    user.name=msg
    await send_msg(sender,"name updated successfully!!")
    user.step="done"

async def handle_update_age(send_msg,msg,user,sender,db):
    if msg.isdigit():
        user.age=msg
        await send_msg(sender,"age updated successfully!!")
        user.step="done"
    else:
        await send_msg(sender,"please enter a valid age!!")
