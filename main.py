import os
import gradio as gr
from dotenv import load_dotenv
from multiagents.agent import MultiAgentTeam
from multiagents.db.database import init_database
from multiagents.db.models import Customer
from multiagents.utils import logger 

log = logger.get_logger(__name__)
log = logger.init(level="DEBUG", save_log=True)


_ = load_dotenv()

UI_PORT: int = int(os.getenv("UI_PORT", "8046"))
DATABASE_URL = os.getenv("DATABASE_URL")




PLACE_HOLDER = "¡Hola! ¿En qué puedo ayudarte?"
BOTH_ICON = "app/assets/bot.png"
USER_ICON = "app/assets/user.png"

# Initialize the agents
multi_agent_team = MultiAgentTeam()

def respond(question, history):
    """ Respond to user input. """
    return  multi_agent_team.request(question)

chatbot = gr.ChatInterface(
    fn=respond,
    type="messages",
    chatbot=gr.Chatbot(elem_id="chatbot", height="auto", avatar_images=[USER_ICON, BOTH_ICON]),
    title="Team Leader Agent with Agno",
    textbox=gr.Textbox(placeholder=PLACE_HOLDER, container=False, scale=7),
    submit_btn="Enviar",
    theme=gr.themes.Default(primary_hue="blue", secondary_hue="indigo"),
    examples=["What is the latest news?", "Who is Thomas Edison?", "How do I make chicken and galangal in coconut milk soup"],
)

if __name__ == "__main__":

    
    # session = init_database()
    # customers = session.query(Customer).all()  # Esto es equivalente a un SELECT * FROM customers
    # for customer in customers:
    #     print(customer.FirstName, customer.LastName, customer.Email)
     
    log.info("Starting UI...")
    chatbot.launch(server_port=UI_PORT)
