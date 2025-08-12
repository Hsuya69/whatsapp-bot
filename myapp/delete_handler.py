
async def handle_delete_user(send_msg,msg,user,sender,db):
    if msg.lower()=="yes":
        await db.delete(user)
        await db.commit()
        await send_msg(sender,"your all details have been deleted")
    else:
        await send_msg(sender,"delete cancelled")
    user.step="done"