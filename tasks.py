from crewai import Task

def create_tasks(topic, researcher, writer,reviewer):

    research_task = Task(
                description=f""" research  the topic: {topic}
                gather:
                -key concepts
                -latest trends
                -benefits and challenges
                -challenges
                """,
                expected_output="detailed research report",
        agent=researcher
    )

    writing_task = Task(
        description=f"""user research report to write a professional blog post on the topic: {topic}
                """,
        expected_output="complete blog article",
        agent=writer
    )

    review_task = Task(
        description=f"""review the blog on the : {topic}
                improve:
                - grammar and spelling
                - readability and clarity
                - structure

                produce a final polished version of the blog article
                """,
        expected_output="final polished blog article",
        agent=reviewer
    )
    return [research_task, writing_task, review_task]
