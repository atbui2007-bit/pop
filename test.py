import random
dwxsfhxdwfhswxh

def generate_text(seed, corpus, length=50):
    words = corpus.split()
    model = {}

    for i in range(len(words) - 1):
        key = words[i]
        value = words[i + 1]
        model.setdefault(key, []).append(value)

    output = [seed]
    for _ in range(length - 1):
        next_options = model.get(output[-1], words)
        output.append(random.choice(next_options))

    return " ".join(output)


if __name__ == "__main__":
    corpus = (
        "AI generated python code can create dynamic text based on simple models. "
        "It can build patterns from input and produce new sentences. "
        "This example uses a basic n-gram style generator to simulate intelligent output."
    )
    print(generate_text("AI", corpus, length=40))

print('I Love Generative AI')
