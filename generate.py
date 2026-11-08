import asyncio
import edge_tts

async def main():
    with open("script.txt", "r", encoding="utf-8") as f:
        text = f.read()

    communicate = edge_tts.Communicate(
        text,
        voice="en-US-AriaNeural",
        rate="+0%",
    )

    await communicate.save("script.mp3")

asyncio.run(main())
