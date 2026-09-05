#!/usr/bin/env python3
class WZMLStyle:

    ST_BN1_NAME = 'Update Channel'
    ST_BN1_URL = 'https://t.me/zonexushubupdates'
    ST_BN2_NAME = 'Leech Group'
    ST_BN2_URL = 'https://t.me/zonexusmlgroup4gb'
    ST_BN3_NAME = 'ZxZone Bot'
    ST_BN3_URL = 'https://t.me/supoorrzx'
    ST_MSG = '<b>Now, this bot will send you all your files and links here. Start using now...</b>'

    ST_BOTPM = '<i>Now, this bot will send all your files and links here. Start Using ...</i>'
    ST_UNAUTH = '<i>You are not an authorized user! Deploy your own ZxZone-Master-MLTB Mirror-Leech bot.</i>'
    OWN_TOKEN_GENERATE = '<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'
    USED_TOKEN = '<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'
    LOGGED_PASSWORD = '<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '<b><u>Generated Temporary Login Token!</u></b>\n<b>Temp Token:</b> <code>{token}</code>\n<b>Validity:</b> {validity}'
    ACTIVATED = 'Activated'
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password.'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    LOG_DISPLAY_BT = 'Log Display'
    WEB_PASTE_BT = 'Web Paste (SB)'
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Miscs'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = 'Help Guide Menu!\n\nNOTE: Click on any CMD to see more minor details.'

    BOT_STATS = '''Bot Statistics:
┖ Bot Uptime : {bot_uptime}

RAM ( MEMORY ) :
┃ {ram_bar} {ram}%
┖ U : {ram_u} | F : {ram_f} | T : {ram_t}

SWAP MEMORY :
┃ {swap_bar} {swap}%
┖ U : {swap_u} | F : {swap_f} | T : {swap_t}

DISK :
┃ {disk_bar} {disk}%
┃ Total Disk Read : {disk_read}
┃ Total Disk Write : {disk_write}
┖ U : {disk_u} | F : {disk_f} | T : {disk_t}
'''

    SYS_STATS = '''OS SYSTEM :
┠ OS Uptime : {os_uptime}
┠ OS Version : {os_version}
┖ OS Arch : {os_arch}

NETWORK STATS :
┠ Upload Data: {up_data}
┠ Download Data: {dl_data}
┠ Pkts Sent: {pkt_sent}k
┠ Pkts Received: {pkt_recv}k
┖ Total I/O Data: {tl_data}

CPU :
┃ {cpu_bar} {cpu}%
┠ CPU Frequency : {cpu_freq}
┠ System Avg Load : {sys_load}
┠ P-Core(s) : {p_core} | V-Core(s) : {v_core}
┠ Total Core(s) : {total_core}
┖ Usable CPU(s) : {cpu_use}
'''
    REPO_STATS = '''Repo Statistics:
┠ Bot Updated : {last_commit}
┠ Current Version : {bot_version}
┠ Latest Version : {lat_version}
┖ Last ChangeLog : {commit_details}

Remarks : <code>{remarks}</code>
'''
    BOT_LIMITS = '''Bot Limitations:
┠ Direct Limit : {DL} GB
┠ Torrent Limit : {TL} GB
┠ GDrive Limit : {GL} GB
┠ YT-DLP Limit : {YL} GB
┠ Playlist Limit : {PL}
┠ Mega Limit : {ML} GB
┠ Clone Limit : {CL} GB
┖ Leech Limit : {LL} GB

Token Validity : {TV}
┠ User Time Limit : {UTI} / task
┠ User Parallel Tasks : {UT}
┖ Bot Parallel Tasks : {BT}
'''

    RESTARTING = '<i>Restarting...</i>'
    RESTART_SUCCESS = '''Restarted Successfully!
┠ Date: {date}
┠ Time: {time}
┠ TimeZone: {timz}
┖ Version: {version}'''
    RESTARTED = '''Bot Restarted!'''

    PING = '<i>Starting Ping...</i>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms...</code>'

    LINKS_START = '''Task Started
┠ Mode: {Mode}
┖ By: {Tag}\n\n'''
    LINKS_SOURCE = '''➲ Source:
┖ Added On: {On}
------------------------------------------
{Source}
------------------------------------------\n\n'''
    PM_START = "➲ Task Started :\n┖ Link: <a href='{msg_link}'>Click Here</a>"
    L_LOG_START = "➲ Leech Started :\n┠ User : {mention} ( #ID{uid} )\n┖ Source : <a href='{msg_link}'>Click Here</a>"
    
    NAME = '{Name}\n\nTask By {User} ( #ID{Id} ) [Link]'
    SIZE = '┠ Size: {Size}\n'
    ELAPSE = '┠ Elapsed: {Time}\n'
    MODE = '┠ Mode: {Mode}\n'
    CREDIT = ''

    L_TOTAL_FILES = '┠ Total Files: {Files}\n'
    L_CORRUPTED_FILES = '┠ Corrupted Files: {Corrupt}\n'
    L_CC = '┖ By: {Tag}\n\n'
    PM_BOT_MSG = '➲ File(s) have been Sent above'
    L_BOT_MSG = '➲ File(s) have been Sent to Bot PM (Private)'
    L_LL_MSG = '➲ File(s) have been Sent. Access via Links...\n'

    M_TYPE = '┠ Type: {Mimetype}\n'
    M_SUBFOLD = '┠ SubFolders: {Folder}\n'
    TOTAL_FILES = '┠ Files: {Files}\n'
    RCPATH = '┠ Path: <code>{RCpath}</code>\n'
    M_CC = '┖ By: {Tag}\n\n'
    M_BOT_MSG = '➲ Link(s) have been Sent to Bot PM (Private)'
    
    CLOUD_LINK = 'Cloud Link'
    SAVE_MSG = 'Save Message'
    RCLONE_LINK = 'RClone Link'
    DDL_LINK = '{Serv} Link'
    SOURCE_URL = 'Source Link'
    INDEX_LINK_F = 'Index Link'
    INDEX_LINK_D = 'Index Link'
    VIEW_LINK = 'View Link'
    CHECK_PM = 'View in Bot PM'
    CHECK_LL = 'View in Links Log'
    MEDIAINFO_LINK = 'MediaInfo'
    SCREENSHOTS = 'ScreenShots'

    STATUS_NAME = '{Name}\n\nTask By {User} ( #ID{Id} ) [Link]'
    mm = ''
    BAR = '\n┟ {Bar}'
    PROCESSED = '\n┠ Processed → {Processed} of {Total}'
    STATUS = '\n┠ Status → {Status}'
    ETA = '\n┠ Time → {ETA}'
    SPEED = '\n┠ Speed → {Speed}'
    ELAPSED = '\n┠ Elapsed → {Elapsed}'
    ENGINE = '\n┠ Engine → {Engine}'
    STA_MODE = '\n┠ In Mode → {InMode}\n┠ Out Mode → {OutMode}'
    SEEDERS = '\n┠ Seeders: {Seeders}'
    LEECHERS = '\n┠ Leechers: {Leechers}'
    CANCEL_BUTTON = '\n┖ Stop → /c_{gid}'
    PROCESSING_STATUS = '\n┠ Processing → {ProcessingStatus}'

    SEED_SIZE = '\n┠ Size: {Size}'
    SEED_SPEED = '\n┠ Speed: {Speed} | '
    UPLOADED = 'Uploaded: {Upload}'
    RATIO = '\n┠ Ratio: {Ratio} | '
    TIME = 'Time: {Time}'
    SEED_ENGINE = '\n┠ Engine: {Engine}'

    STATUS_SIZE = '\n┠ Size: {Size}'
    NON_ENGINE = '\n┠ Engine: {Engine}'

    USER = ''
    ID = ''
    BTSEL = ''
    CANCEL = ''
    mn = '\n\n'

    FOOTER = '\n\n⌬ Bot Stats\n'
    TASKS = '┟ Tasks: {Tasks}\n'
    BOT_TASKS = '┟ Tasks: {Tasks}/{Ttask} | AVL: {Free}\n'
    Cpu = '┟ CPU → {cpu}% | '
    FREE = 'F → {free} [{free_p}%]'
    Ram = '\n┟ RAM → {ram}% | '
    uptime = 'UP → {uptime}'
    DL = '\n┟ DL: {DL}/s | '
    UL = 'UL: {UL}/s'

    PREVIOUS = '⫷'
    REFRESH = '🔄 Refresh'
    NEXT = '⫸'
    PAGE_INFO = 'Page {current}/{total}'

    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '┠ Size: {COUNT_SIZE}\n'
    COUNT_TYPE = '┠ Type: {COUNT_TYPE}\n'
    COUNT_SUB = '┠ SubFolders: {COUNT_SUB}\n'
    COUNT_FILE = '┠ Files: {COUNT_FILE}\n'
    COUNT_CC = '┖ By: {COUNT_CC}\n'

    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    NO_ACTIVE_DL = '''<i>No Active Downloads!</i>

⌬ Bot Stats
┟ CPU → {cpu}% | F → {free} [{free_p}%]
┖ RAM → {ram}% | UP → {uptime}
'''

    USER_SETTING = '''User Settings :
        
┎ Name : {NAME}
┠ ID: <code>{ID}</code>
┠ Telegram DC : {DC}
┖ Language : {LANG}

➲ Available Args:
• <b>-s</b> or <b>-set</b>: Set Directly via Arg
'''

    UNIVERSAL = '''Universal Settings : {NAME}

┎ YT-DLP Options : <b><code>{YT}</code></b>
┠ Daily Tasks : <code>{DT}</code> per day
┠ Last Bot Used : <code>{LAST_USED}</code>
┠ User Session : <code>{USESS}</code>
┠ MediaInfo Mode : <code>{MEDIAINFO}</code>
┠ Save Mode : <code>{SAVE_MODE}</code>
┖ User Bot PM : <code>{BOT_PM}</code>
'''

    MIRROR = '''Mirror/Clone Settings : {NAME}

┎ RClone Config : <i>{RCLONE}</i>
┠ Mirror Prefix : <code>{MPREFIX}</code>
┠ Mirror Suffix : <code>{MSUFFIX}</code>
┠ Mirror Remname : <code>{MREMNAME}</code>
┠ DDL Server(s) : <i>{DDL_SERVER}</i>
┠ User TD Mode : <i>{TMODE}</i>
┠ Total User TD(s) : <i>{USERTD}</i>
┖ Daily Mirror : <code>{DM}</code> per day
'''

    LEECH = '''Leech Settings for {NAME}

┎ Daily Leech : <code>{DL}</code> per day
┠ Leech Type : <i>{LTYPE}</i>
┠ Custom Thumbnail : <i>{THUMB}</i>
┠ Leech Split Size : <code>{SPLIT_SIZE}</code>
┠ Equal Splits : <i>{EQUAL_SPLIT}</i>
┠ Media Group : <i>{MEDIA_GROUP}</i>
┠ Leech Caption : <code>{LCAPTION}</code>
┠ Leech Prefix : <code>{LPREFIX}</code>
┠ Leech Suffix : <code>{LSUFFIX}</code>
┠ Leech Dumps : <code>{LDUMP}</code>
┠ Leech Remname : <code>{LREMNAME}</code>
┖ Leech Metadata : <code>{LMETA}</code>
'''
