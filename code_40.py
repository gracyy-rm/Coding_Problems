# Question : Generate all combinations of Balanced Parantheses

def generate_parantheses(n,open_count=0,close_count=0,path="",result=None):
    if result is None:
        result = []
    if open_count == close_count == n:
        result.append(path)
        return
    if open_count<n:
        generate_parantheses(n,open_count+1,close_count,path + "(",result)
    if close_count<open_count:
        generate_parantheses(n,open_count,close_count+1,path+")",result)
    return result
n=3
print(generate_parantheses(n))