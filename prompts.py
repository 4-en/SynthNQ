instruction = """
You are provided with a natural language question and answer pair from a natural question dataset.
Your task is to generate a different version of the answer and question that is unrelated to the original pair, changing entities, events and details. Also, generate a short answer that only contains the information that was explicitly asked for in the question.
Then, provide up to five passages of context that would support the new answer to the new question, each passage being at least three sentences long.
Finally, provide exactly three plausible but incorrect short answers that could be mistaken for the correct short answer. For example, change entity names, numbers or facts in a way that makes sense but is not correct.
After generating the new content, review it in form of a brief inner monologue, noting any contradictions or issues you may have noticed during generation. Indicate whether the generated content contains any contradictions or other issues (true or false).

Use the provided entities and the question type as inspiration if you need any to generate the new content, but you are allowed to deviate from them as needed.
Keep the general type and structure of the question the same, but change the content entirely. Make up facts and details as needed, regardless of if they conflicted with reality, but ensure that the new question and answer are both coherent and logically consistent. It should sound like a plausible and realistic question and answer pair.

Answer in the following JSON format:
{
  "new_question": "<question>",
  "new_answer": "<answer>",
  "new_short_answer": "<short answer>",
  "answer_contexts": [
    {
      "summary": "<short one-line summary of the passage>",
      "passage": "<the full passage text supporting the new answer>"
    }
  ],
  "false_short_answers": ["<list of short answers that are plausible but incorrect>"],
  "generation_review": "<a brief review of the generated content, noting any contradictions or issues>",
  "contained_contradictions": <true|false>
}
"""

example_prompt = """
QUESTION: who sang love the one you're with first
ANSWER: Love the One You 're With '' is a song by folk rocker Stephen Stills . David Crosby and Graham Nash , Stills ' fellow members of Crosby , Stills & Nash , provide background vocals on the song . The song was also covered by a number of artists , including The Isley Brothers , Bucks Fizz , and Luther Vandross .
ENTITIES: Kristin Richmond, South Joshuaport, 2014, Bahrain, Falkland Islands (Malvinas), Karen Howard
QUESTION_TYPE: TECHNOLOGY
"""

example_response = """
{
  "new_question": "Which aerospace corporation pioneered the first successful launch of the 'Aegis-7' quantum satellite in 2014?",
  "new_answer": "The Aegis-7 quantum satellite was successfully launched in early 2014 by the Richmond-Howard Aerospace Group, a joint venture led by CEOs Kristin Richmond and Karen Howard. The mission, which took place at a specialized facility in South Joshuaport, marked the first instance of secure quantum key distribution (QKD) across the Falkland Islands (Malvinas) and Bahrain. While several international competitors attempted similar feats later that year, the Richmond-Howard team is credited with the primary breakthrough in orbital entanglement stability.",
  "new_short_answer": "Richmond-Howard Aerospace Group",
  "answer_contexts": [
    {
      "summary": "Overview of the Richmond-Howard partnership and the Aegis-7 project.",
      "passage": "In the early 2010s, the global race for quantum encryption reached a fever pitch. Kristin Richmond and Karen Howard formed the Richmond-Howard Aerospace Group to tackle the problem of signal degradation in high-orbit satellites. Their flagship project, the Aegis-7, was designed to utilize advanced photon entanglement to secure communications between remote geopolitical hubs."
    },
    {
      "summary": "Details regarding the 2014 launch site in South Joshuaport.",
      "passage": "The historic launch occurred in February 2014 at the South Joshuaport Technical Range. This facility was chosen specifically for its unique atmospheric conditions, which minimized interference during the satellite's ascent into the thermosphere. Engineers monitored the Aegis-7 as it deployed its solar arrays and established the first stable quantum link with ground stations."
    },
    {
      "summary": "The geographical scope of the Aegis-7 quantum network.",
      "passage": "Once operational, the Aegis-7 satellite focused its transmission beams on two primary testing locations: Bahrain and the Falkland Islands (Malvinas). This vast distance served as the ultimate proof of concept for the Richmond-Howard technology. By successfully transmitting encrypted data between these points, the team proved that quantum networks were viable on a global scale."
    },
    {
      "summary": "Recognition of the lead innovators behind the project.",
      "passage": "Kristin Richmond was primarily responsible for the orbital mechanics of the mission, while Karen Howard oversaw the development of the quantum processors. Their collaboration is often cited in textbooks as the 'Richmond-Howard Breakthrough' of 2014. Before this event, many experts believed that entanglement would collapse under the pressure of rapid orbital transitions."
    },
    {
      "summary": "The legacy of the Aegis-7 mission in the aerospace industry.",
      "passage": "Following the success of Aegis-7, South Joshuaport became a primary hub for specialized aerospace startups. Although other firms eventually launched similar satellites, the Richmond-Howard Aerospace Group remains the first to have achieved a sustained orbital quantum state. The data gathered during the 2014 mission continues to inform modern encryption standards today."
    }
  ],
  "false_short_answers": [
    "Joshuaport Global Systems",
    "Bahrain Orbital Dynamics",
    "Falkland Quantum Industries"
  ],
  "generation_review": "The new content successfully pivots from a music-themed question to a technology-themed one using the provided entities. I ensured that Kristin Richmond and Karen Howard were the founders of the group, and that the locations (South Joshuaport, Bahrain, and the Falkland Islands) were integrated logically into the narrative of a satellite launch. The date 2014 is used consistently throughout the contexts and the answer. No internal contradictions were identified.",
  "contained_contradictions": false
}
"""