import torch


def load_shakespear():
    with open("shakespear.txt") as fn:
        text = fn.read()


def tokenize(text):
    chars = sorted(list(set(text)))

    # Tokenize. Chars -> intergers/index
    s2i = {ch: i for i, ch in enumerate(chars)}
    i2s = {i: ch for i, ch in enumerate(chars)}
    encode = lambda x: [s2i[ch] for ch in x]
    decode = lambda x: [i2s[i] for i in x]

    return encode, decode


# def get_batch(train_data, split):
#     """

#     Args:
#         split (str): "train" or "val"

#     Returns:
#         x,y. x is a batch of context_size characters, y is the next character
#     """
#     # generate a small batch of data of inputs x and targets y
#     data = train_data if split == "train" else val_data
#     ix = torch.randint(len(data) - context_size, (batch_size,))
#     x = torch.stack([data[i : i + context_size] for i in ix])
#     y = torch.stack([data[i + 1 : i + context_size + 1] for i in ix])
#     return x, y
