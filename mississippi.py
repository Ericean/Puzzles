from random import shuffle

def shuffle_and_test(xs,times= 10000):
    count =0
    for i in range(times):
        shuffle(xs)
        for index, item in enumerate(xs):
            if(index < len(xs)-1):
                if(xs[index] == xs[index+1]):
                    count+=1
                    break
    print float(times-count)/float(times)
shuffle_and_test([1,2,3,3,2,3,3,2,4,4,2])
