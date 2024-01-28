
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from ShahmMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✧ اغلاق ✧", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="𝐏𝐥𝐚𝐲", callback_data="resume_cb"),
    ],
    [
            InlineKeyboardButton(text=" 𝐏𝐚𝐮𝐬𝐞 ", callback_data="pause_cb"),
            InlineKeyboardButton(text="𝐒𝐤𝐢𝐩", callback_data="skip_cb"),
            InlineKeyboardButton(text="𝐒𝐭𝐨𝐩", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="✧ اضفني لمجموعتك ✧",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="✧ الاوامر ✧", callback_data="Shahm_help")],
    [
        InlineKeyboardButton(text="", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="", url="https://t.me/SH_AH_M"
        ),
        InlineKeyboardButton(text="✧ مالك البوت ✧", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="✧ اضفني لمجموعتك ✧",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="✧ السورس ✧", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="✧ التحديثات ✧", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="✧ المطور ✧", url="https://t.me/SH_AH_M"
        ),
        InlineKeyboardButton(text="✧ مالك البوت ✧", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="✧ الاوامر ✧",
            callback_data="Shahm_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="✧ اوامر المطور ✧", callback_data="Shahm_cb sudo"),
        InlineKeyboardButton(text="✧ اوامر المالك ✧", callback_data="Shahm_cb owner"),
    ],
    [
        InlineKeyboardButton(text="✧ عودة ✧", callback_data="Shahm_home"),
        InlineKeyboardButton(text="✧ اغلاق ✧", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="✧ السورس ✧", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="✧ عودة ✧", callback_data="Shahm_help"),
        InlineKeyboardButton(text="✧ اغلاق ✧", callback_data="close"),
    ],
]
