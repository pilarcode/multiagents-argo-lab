import os
import gradio as gr
from dotenv import load_dotenv
from lab.agents import MultiAgentTeam
from lab.database import create_database
from lab.utils import logger    

log = logger.get_logger(__name__)

# load the .env file
_ = load_dotenv()
PLACE_HOLDER = os.getenv("PLACE_HOLDER")
BOT_ICON = os.getenv("BOT_ICON")
USER_ICON = os.getenv("USER_ICON")
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH")
SQLITE_DATA_SCRIPT = os.getenv("SQLITE_DATA_SCRIPT")
SQLITE_SCHEMA_SCRIPT = os.getenv("SQLITE_SCHEMA_SCRIPT")
UI_PORT: int = int(os.getenv("UI_PORT", "8046"))



# Initialize the agents
multi_agent_team = MultiAgentTeam()

def respond(question, messages):
    """ Respond to user input. """
    return  multi_agent_team.request(question)

chatbot = gr.ChatInterface(
    fn=respond,
    type="messages",
    chatbot=gr.Chatbot(elem_id="chatbot", height="auto", avatar_images=[USER_ICON, BOT_ICON]),
    title="The Fragance Lab🌺",
    textbox=gr.Textbox(placeholder=PLACE_HOLDER, container=False, scale=7),
    submit_btn="Enviar",
    theme=gr.themes.Default(primary_hue="red", secondary_hue="pink", text_size="lg", radius_size="lg"),
    examples=["Get the product with the highest price 🎁", "What is the fragrance of the day 💕?"],
)

if __name__ == "__main__":
    
    log.info("Creating the database...")
    create_database(schema_sql_path=SQLITE_SCHEMA_SCRIPT, data_sql_path=SQLITE_DATA_SCRIPT, db_path=SQLITE_DB_PATH)
    
    log.info("Starting the UI...")
    chatbot.launch( server_port=UI_PORT, debug=True)
