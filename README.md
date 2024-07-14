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

## Examples
Look at the md files for different examples

### Cold War Agents

###### Starting the game
In the shadowed bunkers of an aging Cold War safe house, an old rivalry reignites in fatal consequence. Victor Petrov, a disillusioned former Soviet agent, harbors deep-seated vengeance against the charismatic double agent, Sergei Ivanov. As Sergei reveals clandestinely collected artifacts of their past in a private reunion, Victor seizes a moment of vulnerability. He quietly laces Sergei's drink with a slow-acting poison he procured during his espionage days. Sipping obliviously, Sergei succumbs to the toxin, seemingly collapsing from a sudden illness. Victor's motive is clear - vengeance for Sergei's betrayal that cost him his life mission.

chat_manager (to Sherlock):

Detective Sherlock, please start questioning the participants (Victor_Petrov, Elena_Rostova, Anton_Volkov).

--------------------------------------------------------------------------------

 USING AUTO REPLY...
Sherlock (to chat_manager):

Question for Victor_Petrov: "Victor, can you tell me about your relationship with Sergei Ivanov and where were you the night he was murdered?"

Understanding of Victor_Petrov: "Gathering insights on Victor's relationship with the victim and establishing his alibi."

Partial Conclusion for Victor_Petrov: "Requires more information to determine his connection and possible motive."

---

Question for Elena_Rostova: "Elena, did you have any recent interactions or disputes with Sergei Ivanov? Where were you the night of the murder?"

Understanding of Elena_Rostova: "Exploring Elena's recent relationship dynamics with Sergei and verifying her whereabouts during the crime."

Partial Conclusion for Elena_Rostova: "Needs more details on her interactions and alibi for the night in question."

---

Question for Anton_Volkov: "Anton, what was your relationship with Sergei Ivanov like? Were you aware of any threats or enemies he may have had recently?"

Understanding of Anton_Volkov: "Examining Anton's relationship and potential knowledge of threats against Sergei."

Partial Conclusion for Anton_Volkov: "More information needed on his relationship and awareness of any threats to Sergei."

---

This will be round one of questioning. Let's continue to gather

--------------------------------------------------------------------------------

Next speaker: Victor_Petrov


 USING AUTO REPLY...
Victor_Petrov (to chat_manager):

Answer to the detective: "Sergei and I worked together many years ago in the intelligence sector. We shared a mutual respect for each other's skills. On the night he was murdered, I was at home, reading an old book and reminiscing the days when life was more thrilling."

--------------------------------------------------------------------------------

Next speaker: Elena_Rostova


 USING AUTO REPLY...
Elena_Rostova (to chat_manager):

Answer to the detective: "No, I haven't had any recent disputes with Sergei Ivanov. We did have a brief chat two days before his death, where he was his usual charismatic self, but nothing out of the ordinary. The night of the murder, I was at home, reading through some old cryptography puzzles."

--------------------------------------------------------------------------------

Next speaker: Anton_Volkov


 USING AUTO REPLY...
Anton_Volkov (to chat_manager):

Answer to the detective: "Sergei and I had a rather amicable relationship, one might say. You know what it's like, old spies and their tales. As for threats, well, Sergei did have a knack for wooing the wrong people sometimes, but nothing I was aware of recently. During the murder? I was keeping an old acquaintance entertained. Victor handed Sergei a drink, but I just thought it was a friendly gesture."

--------------------------------------------------------------------------------

Next speaker: Sherlock


 USING AUTO REPLY...
Sherlock (to chat_manager):

Question for Victor_Petrov: "Victor, can anyone verify your whereabouts that night? Did you communicate with anyone during the time Sergei was murdered?"

Understanding of Victor_Petrov: "Checking the validity of Victor's alibi and if he had any witnesses to support his claim."

Partial Conclusion for Victor_Petrov: "Victor's alibi needs corroboration; his connection with Sergei is long-standing but requires more scrutiny."

---
