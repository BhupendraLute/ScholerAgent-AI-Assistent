import asyncio
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types
from root_agent.agent import root_agent

async def main():
    print("🎓 ScholarAgent AI Started! (Type 'quit', 'exit' or 'bye' to exit)")
    print("You can ask general questions OR paste your notes or syllabus as a text or file path of your choice (e.g., 'C:/notes.pdf')")
    print("-" * 80)

    # Initialize runner once
    APP_NAME = "ScholarAgent"
    session_service = InMemorySessionService()
    runner = Runner(app_name=APP_NAME, agent=root_agent, session_service=session_service)

    # Add USER_ID and SESSION_ID
    USER_ID = "user123"
    SESSION_ID = "session123"

    # Explicitly create the session
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    while True:
        # 1. Accept ANY input (Chat, Questions, or File Paths)
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("👋 Happy studying!")
            break

        print(f"🤖 Agent thinking...")

        # 2. Pass the RAW input to the Root Agent
        user_message_content = types.Content(
            role="user",
            parts=[types.Part(text=user_input)]
        )

        def run_in_thread():
            events = runner.run(
                user_id=USER_ID,
                session_id=SESSION_ID,
                new_message=user_message_content
            )
            
            full_response = ""
            for event in events:
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if part.text:
                            full_response += part.text
            return full_response

        response = await asyncio.to_thread(run_in_thread)
        print(f"🤖 ScholarAgent: {response}")

if __name__ == "__main__":
    asyncio.run(main())