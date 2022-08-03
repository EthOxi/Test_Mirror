from pyrogram import enums

PRE_DICT = {}
CAP_DICT = {}

async def prefix_set(client, message):
    '''  /setpre command '''
    lm = await message.reply_text(
        text="`Setting Up ...`",
    )
    user_id_ = message.from_user.id 
    u_men = message.from_user.mention
    pre_send = message.text.split(" ", maxsplit=1)
    reply_to = message.reply_to_message
    if len(pre_send) > 1:
        txt = pre_send[1]
    elif reply_to is not None:
        txt = reply_to.text
    else:
        txt = ""
    prefix_ = txt
    PRE_DICT[user_id_] = prefix_

    pre_text = await lm.edit_text(f"⚡️<i><b>Custom Prefix Set Successfully</b></i> ⚡️ \n\n👤 <b>User :</b> {u_men}\n🆔 <b>User ID :</b> <code>{user_id_}</code>\n🗃 <b>Prefix :</b> <code>{txt}</code>", parse_mode=enums.ParseMode.HTML)
    

async def caption_set(client, message):
    '''  /setcap command '''

    lk = await message.reply_text(
        text="`Setting Up ...`",
    )
    user_id_ = message.from_user.id 
    u_men = message.from_user.mention
    cap_send = message.text.split(" ", maxsplit=1)
    reply_to = message.reply_to_message
    if len(cap_send) > 1:
        txt = cap_send[1]
    elif reply_to is not None:
        txt = reply_to.text
    else:
        txt = ""
    caption_ = txt
    CAP_DICT[user_id_] = caption_
    try:
        txx = txt.split("#", maxsplit=1)
        txt = txx[0]
    except:
        pass 
    cap_text = await lk.edit_text(f"⚡️<i><b>Custom Caption Set Successfully</b></i> ⚡️ \n\n👤 <b>User :</b> {u_men}\n🆔 <b>User ID :</b> <code>{user_id_}</code>\n🗃 <b>Caption :</b>\n<code>{txt}</code>", parse_mode=enums.ParseMode.HTML)
