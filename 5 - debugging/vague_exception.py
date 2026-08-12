def vague_function(x):
    if type(x) != type(5) and type(x) != type(5.0):
        raise Exception('An error happened. This error message is vague and unhelpful.')
    else:
        print(x / 2)

try:
    vague_function(1)
    vague_function(25)
    vague_function(3.175)
    vague_function('Luan')
except Exception as err:
    print(str(err))