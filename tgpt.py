from openai import OpenAI
from rich.markdown import Markdown
from rich.console import Console
import sys
import os
from rich.progress import Progress
import asyncio

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
console = Console()


async def send_request():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{prompt}"}],
        temperature=0.1,
        stream=True,
    )

    return response


async def ask_chatgpt(prompt):
    console.print(Markdown("# TGPT"))
    q = f"> Prompt: {prompt}"
    console.print(Markdown(q))

    answer = []
    with Progress(transient=True) as progress:
        t = progress.add_task("Waiting...", total=None)
        response = await send_request()

        for event in response:
            event_text = event.choices[0].delta.content
            if event_text:
                answer.append(event_text)

    progress.update(t, completed=100)
    if answer:
        ans = "> ChatGPT:"
        console.print(Markdown(ans))
        console.print(Markdown("".join(answer)), end="")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        prompt = sys.argv[1]
        asyncio.run(ask_chatgpt(prompt))

    else:
        console.print(Markdown("ERROR: INVALID USAGE"))
        console.print(
            Markdown('\n`Usage: $ tgpt "This is my prompt for chatgpt`"'))
