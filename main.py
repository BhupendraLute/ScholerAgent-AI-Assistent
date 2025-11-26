import asyncio
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from root_agent.agent import root_agent

async def main():
    print("🎓 ScholarAgent AI Started! (Type 'quit' to exit)")
    print("You can ask general questions OR paste your notes or syllabus as a text or file path of your choice (e.g., 'C:/notes.pdf')")
    print("-" * 80)

    # Initialize runner once
    APP_NAME = "ScholarAgent"
    session_service = InMemorySessionService()
    runner = Runner(app_name=APP_NAME, agent=root_agent, session_service=session_service)

    while True:
        # 1. Accept ANY input (Chat, Questions, or File Paths)
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("👋 Happy studying!")
            break
        
        # 2. Check if the user just pasted a path (remove quotes just in case)
        clean_input = user_input.strip('"').strip("'")

        print(f"🤖 Agent thinking...")

        # 3. Pass the RAW input to the Root Agent
        response = await runner.run_debug(clean_input)

if __name__ == "__main__":
    asyncio.run(main())