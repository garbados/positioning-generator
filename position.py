import random
import words

template = "For {target}, {product} will {value} more than {other} because {benefit}."

def get_position():
    options = {}
    for field in ['target', 'product', 'value', 'other', 'benefit']:
        options[field] = random.choice(getattr(words, field))
    return template.format(**options)

if __name__ == '__main__':
    print get_position()