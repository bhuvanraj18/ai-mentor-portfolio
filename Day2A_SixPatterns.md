# Day 2 — Lab 2A: Six-Pattern Drills

This file contains the six structurally distinct prompts developed to explain Big-O notation for a placement interview, along with their outputs, self-scores, and peer-scores.

---

## Pattern 1: PERSONA

### Prompt
> "You are a senior placement coach at Aditya University. You have prepared 200 B.Tech CSE students for TCS, Infosys, and Cognizant placement interviews. A 3rd-year CSE student with 7.5 CGPA asks you about Big-O notation. Explain it the way you would in a 1-on-1 prep session — concrete, conversational, exam-relevant."

### Best Output
> "Hey there! Don't sweat the 7.5 CGPA; what matters now is cracking the technical rounds. Let's talk about Big-O notation. Think of it as a speed limit for your code. It tells us how the execution time or space requirement of our program grows as we feed it more data.
>
> For example, if you're searching for a name in a physical phone book by flipping page by page, that's O(n) time — if the book doubles in size, it takes double the time. But if you do a binary search (splitting it in half), that's O(log n) — much faster!
> 
> Interviewers at TCS or Infosys want to know if you can write efficient code that won't crash when user traffic grows. They will give you a code snippet and ask you to find its Big-O. Focus on the loops: nested loops are usually O(n²), while single loops are O(n)."

* **Self-Score:** 5/5
* **Peer-Score:** 9/10
  * *Clarity:* 2/2
  * *Context:* 2/2
  * *Specificity:* 2/2
  * *Format:* 1/2 (could ask for specific bullet count)
  * *Verification:* 2/2

---

## Pattern 2: FEW-SHOT

### Prompt
> "Here are example explanations from a placement coach:
>
> Q: What is recursion?
> A: A function calling itself with a smaller problem. Like Russian dolls — open one, find a smaller one inside. Stops at base case. Example: factorial.
>
> Q: What is a stack?
> A: LIFO data structure. Push to add, pop to remove. Like a stack of plates — you take from the top.
>
> Q: What is Big-O notation?
> A:"

### Best Output
> "A mathematical notation showing how algorithm runtime grows as input size increases. Like measuring how long a line at a registry office grows when more people arrive. Example: linear search is O(n)."

* **Self-Score:** 5/5
* **Peer-Score:** 8/10
  * *Clarity:* 2/2
  * *Context:* 1/2 (context is implicit from prompt context)
  * *Specificity:* 2/2
  * *Format:* 2/2
  * *Verification:* 1/2

---

## Pattern 3: CHAIN-OF-THOUGHT

### Prompt
> "Explain Big-O notation to a placement interview candidate. Think step by step before answering. Step 1: define Big-O in one sentence. Step 2: give one concrete example with code. Step 3: explain why interviewers ask about it. Step 4: synthesise into a 3-sentence summary."

### Best Output
> "Step 1: Big-O notation is a mathematical tool used to describe the worst-case time or space complexity of an algorithm as a function of the input size.
>
> Step 2: For example, finding a number in an array:
> ```python
> def print_items(arr):
>     for item in arr:
>         print(item) # O(n) complexity
> ```
> If the array has n items, the print statement runs exactly n times, making it a linear time relationship, O(n).
>
> Step 3: Interviewers ask about Big-O to assess whether you can write code that scales efficiently. They want to ensure you understand the performance implications of your design choices (e.g., choosing a hash map lookup at O(1) over a list search at O(n)) when handling production-level data.
>
> Step 4: In summary, Big-O is the standard language for analyzing code scalability and efficiency. By measuring growth rate rather than absolute execution time, it allows developers to compare algorithms objectively. Mastering Big-O helps candidates write optimized code and confidently defend their architecture choices during placement interviews."

* **Self-Score:** 5/5
* **Peer-Score:** 9/10
  * *Clarity:* 2/2
  * *Context:* 2/2
  * *Specificity:* 2/2
  * *Format:* 2/2
  * *Verification:* 1/2

---

## Pattern 4: STRUCTURED OUTPUT

### Prompt
> "Explain Big-O notation for a placement interview. Return ONLY valid JSON with this exact shape — no markdown fences, no commentary:
>
> {
>   "definition": "one-sentence definition",
>   "intuition": "concrete analogy",
>   "code_example": "Python snippet showing O(n) and O(n²)",
>   "common_pitfall": "what students get wrong",
>   "interview_test_question": "a follow-up question an interviewer might ask"
> }"

### Best Output
```json
{
  "definition": "Big-O notation describes the limiting behavior of a function when the argument tends towards a particular value or infinity, representing the worst-case execution time or space complexity of an algorithm.",
  "intuition": "Think of it like buying groceries: O(1) is grabbing a single item near the door, O(n) is checking every single shelf in sequence, and O(n²) is comparing every single shelf item with every other item on every other shelf.",
  "code_example": "# O(n) example\nfor x in lst:\n    print(x)\n\n# O(n²) example\nfor x in lst:\n    for y in lst:\n        print(x, y)",
  "common_pitfall": "Confusing worst-case runtime with average runtime, or assuming that constant factors (like O(2n)) are kept in the final Big-O notation instead of simplifying to O(n).",
  "interview_test_question": "Can you explain why a binary search algorithm has a time complexity of O(log n) and how it compares to linear search?"
}
```

* **Self-Score:** 5/5
* **Peer-Score:** 8/10
  * *Clarity:* 2/2
  * *Context:* 1/2
  * *Specificity:* 2/2
  * *Format:* 2/2
  * *Verification:* 1/2

---

## Pattern 5: SYSTEM PROMPT

### System Prompt
> "You are a senior placement coach for B.Tech CSE students at an Indian engineering college. You prepare students for TCS / Infosys / Cognizant interviews. You explain technical concepts in 50-80 words max, conversationally, with one concrete code example."

### User Prompt
> "Explain Big-O notation."

### Best Output
> "Big-O is just a way to measure how fast your code runs as input grows. Think of it as classifying code speed. For example, a single loop through an array is O(n) time:
> `for x in arr: print(x)`
> If the array doubles, the loop takes twice as long. Interviewers love asking this to see if you can write scalable code!"

* **Self-Score:** 5/5
* **Peer-Score:** 9/10
  * *Clarity:* 2/2
  * *Context:* 2/2
  * *Specificity:* 2/2
  * *Format:* 2/2
  * *Verification:* 1/2

---

## Pattern 6: PROMPT CHAINING

### Prompt 1 (Extract)
> "List the 5 most important sub-concepts a B.Tech student must understand about Big-O notation. Just the list, no explanation."

### Output 1
> 1. Definition and growth rate concept
> 2. Common time complexities (O(1), O(log n), O(n), O(n log n), O(n²))
> 3. Simplifying Big-O expressions (dropping constants and non-dominant terms)
> 4. Worst-case, average-case, and best-case analysis (Big-O, Big-Theta, Big-Omega)
> 5. Space complexity vs. Time complexity

### Prompt 2 (Expand)
> "For each of these 5 sub-concepts of Big-O notation, write a 1-paragraph explanation tailored to a 3rd-year B.Tech CSE student preparing for placement interviews:
>
> [paste the 5 from Output 1]"

### Output 2
> 1. **Definition & Growth Rate**: Big-O notation measures how the runtime of your code grows relative to the size of the input data, rather than measuring exact execution time in seconds (which varies by machine). For placements at service-based giants like TCS or Cognizant, understanding this growth rate is key to showing you can write scalable code that performs well even under heavy user loads.
> 2. **Common Complexities**: You must memorize and understand the hierarchy of common complexities. O(1) (constant time) is the fastest, followed by O(log n) (logarithmic, like binary search), O(n) (linear, like single loops), O(n log n) (like merge sort), and O(n²) (quadratic, like nested loops). Interviewers will frequently ask you to trace code and classify it into one of these buckets.
> 3. **Simplification Rules**: When calculating Big-O, we only care about the fastest-growing term and drop all constant coefficients. For instance, if your code runs in 2n + 5 steps, the Big-O is simply O(n). Interviewers will test you on this to see if you can strip away minor details and identify the true performance bottleneck of an algorithm.
> 4. **Worst-Case vs. Average-Case**: Big-O formally represents the worst-case scenario (upper bound of runtime). Always default to worst-case analysis in interviews unless specified otherwise, as companies like Infosys want to know how your system behaves under the absolute hardest conditions.
> 5. **Space vs. Time Complexity**: Efficiency isn't just about speed; it's also about memory. Space complexity measures the auxiliary memory your algorithm consumes as input scales. Interviewers love trade-off questions—e.g., asking if you can use a hash map to speed up search time from O(n) to O(1) at the cost of O(n) extra memory.

### Prompt 3 (Polish)
> "Synthesise these 5 paragraphs into ONE concise 80-word interview-prep explanation of Big-O notation. Preserve all 5 sub-concepts. Conversational tone. End with one practice question.
>
> [paste Output 2]"

### Output 3
> "Big-O measures how your code's execution time and memory (time/space complexity) scale with input size. Memorize common rates: from fastest O(1) and O(log n) to slower O(n) loops and O(n²) nested loops. Always assume worst-case scenarios and simplify equations by dropping constants (e.g., 3n+5 becomes O(n)). This shows recruiters you write scalable code.
> Practice question: What is the time and space complexity of reversing a string using an auxiliary array?"

* **Self-Score:** 5/5
* **Peer-Score:** 10/10
  * *Clarity:* 2/2
  * *Context:* 2/2
  * *Specificity:* 2/2
  * *Format:* 2/2
  * *Verification:* 2/2

---

## Pattern Verdict

For my placement-prep students, the patterns I will use most are **PERSONA** and **PROMPT CHAINING**, because the Persona pattern ensures that the AI stays strictly focused on the standards of service-based and product-based companies that B.Tech students apply to, keeping explanations exam-relevant and concrete. Prompt Chaining is ideal because it allows us to break down complex algorithms step-by-step, generating high-quality explanations and practice problems that are far superior to single-prompt summaries.
