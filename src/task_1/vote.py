def vote(votes):
    result = 0
    q = 0
    for i in votes:
        n = votes.count(i)
        if n > q:
            q = n
            result = i
    return result




    
if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))