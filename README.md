# Alex.AI

**1st Prize in the National AI Student Challenge 2024, Track 3**

Greetings! I am Alex, a tool that is used to assist students and working software engineers in speeding up their software engineering needs!

## What is Alex.AI?

Alex.AI is an application powered by a large-language model (LLM) that assists software engineers with their needs in the early stages of the software development lifecycle (SDLC).

### The Problem

- The “analysis” and “design” phases in the software development lifecycle (SDLC) are phases whereby developers take the requirements gathered in the planning phase, analyse these requirements to software use cases, and then translate them into plans to implement the solution.
  
- In these phases, several diagrams are typically created, such as use-case diagrams and use-case descriptions to illustrate the use cases of the software product,  as well as other diagrams that represent the entire architecture of the software, such as class diagrams and component diagrams, allowing developers to get a proper overview of how software components interact with one another.
  
- These deliverables necessitate days of examining requirements documents and frequent discussions and debates between engineers, which can be time-consuming and mentally draining. In addition, these diagrams are time-consuming to produce manually (through the use of tools such as draw.io or Lucidchart)

### The Solution

The solution is an application powered by an LLM - using the power of prompt engineering and deep learning to enhance the analysis and design phases of the SDLC. The application is capable of performing the following tasks:

1. Use Case Description generation
2. Use Case Diagram generation
3. Identifying potential candidate classes from the software requirements
4. Class diagram generation
5. Component diagram generation

### Prompt Engineering Techniques Used

#### Few-shot prompting

Few-shot prompting was for generating use case diagrams based on the requirements. As shown below, several "example" outputs are used as prompts to inform the model of generating the use case to requirements mapping and the actor to use case mappings:

```
template = f"""
    Based on these requirements, I will like you to generate for me a use case diagram.
    
    Here are the requirements:
    {requirements}

    In addition, explain the use cases and actors in the following format:

    Use case to requirements mapping:

    Use Case 1: Satisfies requirements 1 and 2 as ...
    Use Case 2: Satisfies requirements 3 as ...
    ...

    Actor to use case mapping:

    Actor 1: Uses Use Case 1 and 2 as ...
    Actor X: ...

    @startuml

    <PlantUML code here>

    @enduml 

"""
```
#### Chain-of-thought prompting

Chain-of-thought prompting is used to generate the class diagram based on the requirements, necessitating a breakdown of complex task of creating a class diagram into smaller steps, such as identifying relationships between classes, providing examples of relationship types, as well as explaining the rationale of the relationship types chosen.

```
template = f"""
    Your task now is to refine a UML class diagram by introducing proper relationships between the previously identified candidate classes in your previous response. Do NOT change or remove the methods and attributes inside the candidate classes.

    Based on the candidate classes and their descriptions provided earlier, your goal is to:

    1. Identify the Types of Relationships: For each pair of classes, determine the most appropriate relationship type. Consider the nature of their interaction based on the software requirements. Only use the relationships below:

    **Association** 

    * **Syntax:** 
    ```plantuml
    classOne -- classTwo
    ```
    **Inheritance:**

    * **Syntax:**
    ```plantuml
    class Subclass <|-- Superclass 
    ```

    **Realization (Interface)**

    * **Syntax:**
    ```plantuml
    interface InterfaceName <|.. ImplementingClass 
    ```

    **Dependency:**

    * **Syntax:**
    ```plantuml
    class DependentClass ..> IndependentClass
    ```

    **Aggregation:**

    * **Syntax:**
    ```plantuml
    class Whole o-- Part 
    ```

    **Composition:**

    * **Syntax:**
    ```plantuml
    class Whole *-- Part
    ```

    2. Specify Multiplicity: Only when it is needed to clarify, provide multiplicity for the relationships. This will clarify how many instances of a class can be associated with instances of another class. Follow the guideline below:

    In class diagrams, multiplicity symbols (like "0..*" or "1") explain how many objects of one class can link to another. Show multiplicity when it clarifies the relationship's meaning, especially for ownership (aggregation/composition) or cardinality (one-to-one, one-to-many). For clear, simple relationships, you can sometimes omit it for better readability.

    After updating the UML diagram, please provide a summary of the class diagram, including the type of relationship established between each pair of classes and your rationale for these decisions.

    Follow this response template:

    <Summary of relationships here>

    <Rationale>

    @startuml
    skinparam linetype ortho
    <UML diagram here>
    @enduml
"""
```

#### Tuning-of-Thought prompting

Tuning-of-Thought prompting allows for iterative refinement of the generated diagrams.  This is when the user provides targeted feedback on the initial diagram output, prompting the AI to make specific adjustments.

```
template = f""" 
    Make the following changes to the UML diagram that you have generated prior based on the changes listed below:

    {changes}

    Follow this template:

    @startuml

        <UML diagram here>

    @enduml

    In addition, explain the changes that you have made to the UML diagram, and provide your justification for each change made.

"""
```

### Advantages of Alex.AI

1. Saves time by eliminating trial-and-error in crafting prompts for complex diagrams.
2. Reduces knowledge barrier as allowing users of any proficiency level to create quality diagrams.
3. Explains the rationale behind the diagrams generated which indirectly teaches software design principles.


## Usage

- Before running the program, ensure that you have the following libraries (more details on the requirements can be found in the `requirements.txt` file):
  - streamlit
  - streamlit_extras
  - langchain-openai
  - plantuml
  - validators

- Clone the repository
- In the `keys.txt` file, replace `YOUR_API_KEY` with your own OpenAI API key
- Run the program using `streamlit run Home.py`
- Once the program is running, you can access it through your web browser. Streamlit applications should be accessible at `localhost:8501`.
- Follow the on-screen instructions and interact with the application depending on whether you are dealing with a class diagram, component diagram, or User-centered design (UCD) with your prompt. <br />

Should you encounter any issues or have feedback, please share it with us.

## Technologies Used

- Python
- Langchain
- Streamlit
- GPT-4 Turbo Model
