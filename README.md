# MerdaOS
_Voice Assistant Merda based on ChatGPT, ready to answer any of your queries, as well as can perform any of your commands._
>The Merda is launching by pronouncing the wake word "Merda"

## Features

- Ability to work with ChatGPT
- Play music and control it
- Ability to add many different commands
- Handy config file

## Commands
The ability to add commands is in commands.py
> Here you must enter the command, the name of the command and its trigger
```py
commands_list = [
    {"time": "current time"}
]
```
> Next, write command handler in this method
```py
def executeCommand(text: str):
    command_type, trigger = getType(text)
    print("Executing the command...")
    if command_type == "time":
        now = datetime.now().time()
        hours = num2words(now.hour, lang='ru')
        minutes = num2words(now.minute, lang='ru')
        text_to_speech.text_to_audio(f"The current time is now {hours} hours {minutes} minutes")
    print("Command executed!")
```
Done! The command now works.

## Installation
> Python version >= 3.9.5 is recommended.

Merda requires mostly libraries:
- pyttsx3
- pvrecorder
- pvporcupine
- openai
- pvcobra

These models are also required:
- Vosk model small
- Porcupine wake word model