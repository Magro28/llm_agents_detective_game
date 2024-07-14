# pip install pyautogen

import os, json, logging
import autogen
from openai import OpenAI


logger = logging.getLogger(__name__)
logging.basicConfig(filename="app.log", filemode="w", level=logging.DEBUG)

llm_config = {
    "config_list": [
        {
            "api_key": str(os.environ["OPENAI_API_KEY"]),
            "model": "gpt-4o",
            "temperature": 1,
            "max_tokens": 256,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
        }
    ],
}

generated_world = {}


def generate_game(topic):

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": """You are a game generator for a detective game with the topic: """
                        + topic
                        + """. 
            Your job is to generate a new game where one player is a murderer, 2 Players are innocent citicens. 
            All of the players where at the time of the murder at the same place and saw different things which could be helpful for the detective but also things which are could bring him on a false track. 
            You create a detailed murder plot how the murderer killed the victim (non-Player) and their motive. Then generate a short summary of the backstories of each player and the victim. Please always describe the characteristics of the players in the backstory (like depressive, fearful, playboy, likes to flirt with everyone, etc..), build in small motives for everyone and some small indications of what each player noticed at the time related to the case. Always use the names of the players in the plot and backstories.
            The game is that the detective can now ask all the Players to solve the case with their Information. The murderer is of Course lying. You generate json as string which Looks like this for the murderer and the other Players:

{"true_murder_story" : "...", "victim": {"name": "...", backstory: "..."}, "player_1" : {"name" : "...", "backstory": "...", "is_murderer" : "True/False"}, "player_2" : {...}}


Only respond with json as string! Do not respont with Chat. This is a technical function""",
                    }
                ],
            }
        ],
        temperature=1,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    generated_game = response.choices[0].message.content
    logger.debug(generated_game)
    json_content = "{" + generated_game.split("{", 1)[1].rsplit("}", 1)[0] + "}"
    logger.info("JSON CONTENT:" + json_content)

    return json.loads(json_content)


def load_config(file_path):

    with open(file_path, "r") as file:
        file_content = file.read()

    return file_content


def generate_player_instructions(generated_world):
    detective_instructions = (
        load_config("./config/detective.conf")
        .replace("VICTIM_NAME", generated_world.get("victim", {}).get("name"))
        .replace("VICTIM_BACKSTORY", generated_world.get("victim", {}).get("backstory"))
    )
    murderer_instructions = (
        load_config("./config/murderer.conf")
        .replace("VICTIM_NAME", generated_world.get("victim", {}).get("name"))
        .replace("VICTIM_BACKSTORY", generated_world.get("victim", {}).get("backstory"))
        .replace("TRUE_MURDER_STORY", generated_world.get("true_murder_story", {}))
    )
    player_instructions = (
        load_config("./config/player.conf")
        .replace("VICTIM_NAME", generated_world.get("victim", {}).get("name"))
        .replace("VICTIM_BACKSTORY", generated_world.get("victim", {}).get("backstory"))
    )

    return detective_instructions, murderer_instructions, player_instructions


def start_game(llm_config, generated_world):

    logger.info(generated_world.get("true_murder_story"))
    print(generated_world.get("true_murder_story"))

    detective_instructions, murderer_instructions, player_instructions = generate_player_instructions(generated_world)

    detective = autogen.ConversableAgent(
        name="Sherlock",
        system_message=detective_instructions,
        llm_config=llm_config,
        is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
    )

    player_1 = autogen.ConversableAgent(
        name=generated_world.get("player_1", {}).get("name").replace(" ", "_").replace('\'', ''),
        system_message=(
            "You are involved in a murder case." + murderer_instructions
            if generated_world.get("player_1", {}).get("is_murderer") == "True"
            else player_instructions
            + " Your backstory is: "
            + generated_world.get("player_1", {}).get("backstory")
            + ". You will write like your personality is described."
        ),
        llm_config=llm_config,
        is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
    )

    player_2 = autogen.ConversableAgent(
        name=generated_world.get("player_2", {}).get("name").replace(" ", "_").replace('\'', ''),
        system_message=(
            "You are involved in a murder case. " + murderer_instructions
            if generated_world.get("player_2", {}).get("is_murderer") == "True"
            else player_instructions
            + " Your backstory is: "
            + generated_world.get("player_2", {}).get("backstory")
            + " You will write like your personality is described."
        ),
        llm_config=llm_config,
        is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
    )

    player_3 = autogen.ConversableAgent(
        name=generated_world.get("player_3", {}).get("name").replace(" ", "_").replace('\'', ''),
        system_message=(
            "You are involved in a murder case. " + murderer_instructions
            if generated_world.get("player_3", {}).get("is_murderer") == "True"
            else player_instructions
            + " Your backstory is: "
            + generated_world.get("player_3", {}).get("backstory")
            + " You will write like your personality is described."
        ),
        llm_config=llm_config,
        is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
    )

    groupchat = autogen.GroupChat(
        agents=[detective, player_1, player_2, player_3],
        messages=[],
        max_round=50,
        speaker_selection_method="round_robin",
    )
    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config=llm_config,
        is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
    )

    manager.initiate_chat(
        detective,
        message="Detective Sherlock, please start questioning the participants ("
        + generated_world.get("player_1", {}).get("name").replace(" ", "_")
        + ", "
        + generated_world.get("player_2", {}).get("name").replace(" ", "_")
        + ", "
        + generated_world.get("player_3", {}).get("name").replace(" ", "_")
        + ").",
    )


# main function for the application
if __name__ == "__main__":
    print("Please enter the general topic of the detective game. ")
    topic = input("TOPIC: ")
    print("You entered the topic: " + topic)

    print("Generating new game")
    generated_world = generate_game(topic)

    print("Starting the game")
    start_game(llm_config, generated_world)
    # type exit to terminate the chat

    pass
