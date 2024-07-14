# LLM Agent Sherlock - The detective game
A large language model powered multi agent detective game using openai and autogen

## Game Rules
A game master creates the case and the background for all players from a user given topic.
Sherlock the detective can ask all players and try to unravel the mysterys.
One of the players is the true murderer and tries to hide this.
The game runs in round robin style where Sherlock asks all his questions in a group chat with the players. Then the players can answer these.
After a while Sherlock will end the investigation and announces the murderer

## Issues
* Sherlock seems to confuse names afer a while
* Sherlock seems sometimes to blame a complete outstander as the murderer
* The game master creates a broken case
