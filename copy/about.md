# About
The Voice Bot is a real-world application designed to demonstrate the practical uses of AI technology. It allows users to explore and engage in conversations about the Voice Referendum and broader topics related to voice. The bot showcases AI’s ability to facilitate informed and dynamic discussions, making complex subjects accessible and understandable

# Privacy
Data is not recorded, stored, or viewable by the author. All code is open and can be reviewed in the GitHub repository (here) [https://github.com/acousland/theVoiceBot], ensuring transparency in data handling and processing. For OpenAI API privacy policy, refer to [OpenAI](https://openai.com/enterprise-privacy). As at October 2023, the OpenAI API platform may "securely retain API inputs and outputs for up to 30 days to identify abuse" but they will not use the data for further training models "We do not use your business data, inputs, or outputs for training our models." 

# Training Sources
The Voice Bot is primarily informed by [official yes | no referendum pamphlet](https://www.aec.gov.au/referendums/files/pamphlet/your-official-yes-no-referendum-pamphlet.pdf) from the Australian Electoral Commission. This document has been summarised to develop the core issues the bot discusses, with all efforts made to maintain an unbiased perspective. However, complete impartiality is challenging, and some bias may persist. Users are encouraged to introduce diverse arguments to enrich the conversation.

# Architecture
The Voice Bot’s core is built with Python and utilises [LangChain](https://www.langchain.com) to streamline the abstraction of the of LLM into application. [Streamlit](https://streamlit.io), an open-source platform, is employed for crafting the user interface, enabling the creation of interactive and user-friendly applications with Python. The underlying language processing capabilities are powered by OpenAI's [ChatGPT-4](https://openai.com/gpt-4). The codebase is publicly available for review and contributions on GitHub https://github.com/acousland/theVoiceBot

# Limitations and Ethical Issues
## Accuracy of Information
Large Language Models (LLMs) like the one powering this chatbot occasionally "hallucinate" or generate information that isn't entirely accurate or may be a product of the model's vast training data, rather than a reflection of factual reality. As such, while the AI strives to provide accurate and relevant information, there's potential for unintentional errors or omissions. Users are strongly urged to fact-check any information provided and consult multiple authoritative sources to ensure accuracy and comprehensiveness.

## Limited Scope of Information
The Voice Bot operates with the limitation of being informed by a confined dataset, derived primarily from the official Australian Electoral Commission's information and the GPT-4’s training cut-off in September 2021. This could limit the diversity of perspectives offered. The bot might not incorporate recent developments related to the referendum, potentially limiting the depth of conversations and insights provided. Users should be aware of these constraints and consider seeking additional sources of information to obtain a more comprehensive viewpoint.

## Complexity and Insensitivity
The Voice Referendum touches upon intricate and sensitive social values that are deeply held by many individuals. Given the complexity of these issues, the provided training data and the current capabilities of AI might not capture all the nuances, potentially leading to hasty or unintended positions. Users are reminded that interactions with the bot should be treated as informal conversations rather than definitive stances on these profound topics. Be cautious and considerate, recognising the limitations and not taking any part of the discussion to heart or as a personal affront.

## Balance Fallacy
A potential limitation in The Voice Bot is that while it is designed to enable dynamic and enriching dialogues, it may inadvertently fall victim to the "balance fallacy." This issue arises when the application allocates equal importance to both sides of a debate, neglecting the disparity in empirical evidence or logical consistency that might exist between them. Consequently, users may experience an imbalanced representation of arguments, where the objective rationality of each perspective is not adequately portrayed.

## Compromising Human Autonomy
Users need to be particularly cautious of the potential for AI to inadvertently disempower individuals in the democratic process. Relying heavily on AI for information and decision-making can lead to an erosion of critical thinking and personal agency. It can foster a passive consumption of information, where individuals become overly dependent on automated systems, potentially marginalising human perspectives and experiences. This undue reliance may skew public discourse, dilute the richness of democratic debates, and ultimately compromise the authenticity and inclusivity of electoral processes. The author emphasises the importance of balancing AI interaction with active engagement in diverse information sources and critical, independent thinking to uphold the democratic principles of participation, debate, and decision-making.

# Disclaimer
The information provided by The Voice Bot is for informational purposes only and not to be considered professional advice. The author makes no guarantees regarding the accuracy or completeness of the responses. Users are advised to seek expert advice for specific needs. The author shall not be liable for any damages or losses arising from the use of The Voice Bot. Use of this bot signifies acceptance of this disclaimer.

It’s imperative to highlight that the opinions and information provided by the bot do not mirror the author's personal beliefs or standpoints, nor those of any past or present employers. The bot is designed to operate independently, with its responses generated based on programmed algorithms and artificial intelligence, not influenced or directed by the individual perspectives of the author or any associated organisations.

# License
This software is licensed under the GNU General Public License version 3 (GPLv3), permitting users to freely use, modify, and distribute it. All derived works of this software must also be open source and carry the same license to maintain the openness and freedom of the software. GPLv3 ensures that the software and its derivatives remain accessible and modifiable to all users, promoting innovation and collaboration. License can be viewed (here)[https://www.gnu.org/licenses/gpl-3.0.en.html]

# Authorship
Developed by Aaron Cousland [LinkedIn](https://www.linkedin.com/in/aaron-cousland/)