from dotenv import load_dotenv
import os
from automation import AutomationWeb

load_dotenv()
EMAIL_AKUN = os.getenv("EMAIL")
PASSWORD_AKUN = os.getenv("PASSWORD")
LINK_WEBSITE = os.getenv("LINK_LOGIN")

# print(f"{EMAIL_AKUN}, {PASSWORD_AKUN}, {LINK_WEBSITE}")

if __name__ == "__main__":
    bot_satu = AutomationWeb(EMAIL=EMAIL_AKUN, PASSWORD=PASSWORD_AKUN, LINK_LOGIN=LINK_WEBSITE)
    bot_satu.log_navigate_make_list_add_card(name_of_board="love", list_name="Todo", card_content="Make Regsiter Page")
    # bot_satu.log_make_board_make_list_add_card(board_name="Mami", list_name="Too do", card_content="Backend API")