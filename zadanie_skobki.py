def valid(string):
    if str(string).replace(' ', '') == '':
        print(False)
    elif int(len(string))%2 == 0:
        
        a = list(string)
        finalsum = 0          
        
        if a[0] == ')' or a[0] == '}' or a[0] == ']':
            print(False)
            
        else:
                
            for i in range(int(len(string)/2)):
                if (str(a[i]) == '(' or str(a[i]) == '[' or str(a[i]) == '{') == (str(a[len(string)-1]) == ')' or str(a[len(string)-1]) == ']' or str(a[len(string)-1]) == '}'):
                        finalsum+=1
                
                else:
                    continue
                        
            if finalsum == len(string)/2:
                print(True)
            elif finalsum !=len(string)/2:

                p = 0
                for i in range(0, len(string), 2):
                    a = list(string)
                    if ((str(a[i]) == '(' and str(a[i+1]) == ')') or ((str(a[i]) == '[' and str(a[i+1]))) == ']') or ((str(a[i]) == '{' and str(a[i+1]) == '}')):
                        p+=1
                
                if p == len(string)/2:
                    print(True)
                else:
                    print(False)
                                
    else:
        print(False)
