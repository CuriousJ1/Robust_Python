# Introduction to Robust Python

Always construct a software design that is so simple that there are obviously no deffeciencies.

## Coding examples

### Version 1
This function takes a recipe and adjusts every ingredient to handle a new number of
servings. However, this code prompts many questions.
• What is the pop for?
• What does recipe[0] signify? Why is that the old servings?
• Why do I need a comment for numbers that will be easily measurable?

### Version 2
Those who favor clean code probably prefer the second version (I certainly do). No raw loops. Variables do not mutate. I’m returning a dictionary instead of a list of tuples. All these changes can be seen as positive, depending on the circumstances. But I may have just introduced three subtle bugs.
• In the original code snippet, I was clearing out the original recipe. Now I am not. Even if it’s just one area of calling code that is relying on this behavior, I broke that calling code’s assumptions.
• By returning a dictionary, I have removed the ability to have duplicate ingredi‐ ents in a list. This might have an effect on recipes that have multiple parts (such as a main dish and a sauce) that both use the same ingredient.
• If any of the ingredients are named “servings” I’ve just introduced a collision with naming.

### Version 3
This looks much better, is better documented, and expresses original intent clearly. The original developer encoded their ideas directly into the code. From this snippet, you know the following is true:
• I am using a Recipe class. This allows me to abstract away certain operations. Presumably, inside the class itself there is an invariant that allows for duplicate ingredients. (I’ll talk more about classes and invariants in Chapter 10.) This pro‐ vides a common vocabulary that makes the function’s behavior more explicit.
• Servings are now an explicit part of a Recipe class, rather than needing to be the first element of the list, which was handled as a special case. This greatly simpli‐ fies calling code, and prevents inadvertent collisions.
• It is very apparent that I want to clear out ingredients on the old recipe. No ambiguous reason for why I needed to do a .pop(0).
• Ingredients are a separate class, and handle fractions rather than an explicit float. It’s clearer for all involved that I am dealing with fractional units, and can easily do things such as limit_denominator(), which can be called when people want to restrict measuring units (instead of relying on a comment).
I’ve replaced variables with types, such as a recipe type and an ingredient type. I’ve also defined operations (clear_ingredients, adjust_proportion) to communicate my intent. By making these changes, I’ve made the code’s behavior crystal clear to future readers. They no longer have to come talk to me to understand the code. Instead, they comprehend what I’m doing without ever talking to me. This is asyn‐ chronous communication at its finest.

### Collections

List
This is a collection to be iterated over. It is mutable: able to be changed at any time. Very rarely do you expect to be retrieving specific elements from the mid‐ dle of the list (using a static list index). There may be duplicate elements. The cookbooks on a shelf might be stored in a list.

String
An immutable collection of characters. The name of a cookbook would be a string.

Generator
A collection to be iterated over, and never indexed into. Each element access is performed lazily, so it may take time and/or resources through each loop itera‐ tion. They are great for computationally expensive or infinite collections. An online database of recipes might be returned as a generator; you don’t want to fetch all the recipes in the world when the user is only going to look at the first 10 results of a search.

Tuple
An immutable collection. You do not expect it to change, so it is more likely to extract specific elements from the middle of the tuple (either through indices or unpacking). It is very rarely iterated over. The information about a specific cook‐ book might be represented as a tuple, such as (cookbook_name, author, page count).

Set
An iterable collection that contains no duplicates. You cannot rely on ordering of elements. The ingredients in a cookbook might be stored as a set.

Dictionary
A mapping from keys to values. Keys are unique across the dictionary. Dictionar‐ ies are typically iterated over, or indexed into using dynamic keys. A cookbook’s index is a great example of a key to value mapping (from topic to page number.)

### Iteration
for loops
for loops are used for iterating over each element in a collection or range and performing an action/side effect.

while loops
while loops are used for iterating as long as a certain condition is true.

Comprehensions
Comprehensions are used for transforming one collection into another (nor‐ mally, this does not have side effects, especially if the comprehension is lazy).

Recursion
Recursion is used when the substructure of a collection is identical to the struc‐ ture of a collection (for example, each child of a tree is also a tree).

### Law of least suprises
when someone reads through the codebase, they should almost never be surprised at behavior or implementation (and when they are sur‐ prised, there should be a great comment near the code to explain why it is that way). This is why communicating intent is paramount. Clear, clean code lowers the likeli‐ hood of miscommunication.