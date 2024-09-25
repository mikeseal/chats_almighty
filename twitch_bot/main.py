from os import getenv
from dotenv import load_dotenv
from twitch_bot.controller.chat_bot_controller import ChatBotController
from pathlib import Path
from model.models import Channels, Commands, Links

# INFO this is the starting point of our program, it creates the controller which glues the model+view components together
if __name__ == '__main__':
    load_dotenv()
    chat_bot = ChatBotController(getenv("TWITCH_CLIENT_ID"), getenv("TWITCH_CLIENT_SECRET"),
                                 Path("dont_show_on_stream.json"),
                                 "shepsalmighty")

    chat_bot.run()





    model_channels = Channels()
    model_commands = Commands())
    model_links = Links()
    
    

    view = UserView()
    controller = UserController(model, view)
    controller.add_user("Alice")
    controller.add_user("Bob")
    controller.show_users()
if __name__ == "__main__":
    main()