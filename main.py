from agents import researcher, writer, reviewer
from tasks import create_tasks
from crew import create_crew

TOPIC = input("Enter the topic for the report: ")

tasks= create_tasks(TOPIC, researcher, writer, reviewer)
crew = create_crew(researcher, writer, reviewer, tasks)

result = crew.kickoff()

print("\n")
print("=" * 80)
print("FINAL RESULT")
print("=" * 80)
print(result)

# if __name__ == "__main__":
#     main()