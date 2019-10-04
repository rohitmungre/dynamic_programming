import copy
st = 'bab.aaay'
rex = '.a*b..*y'

def regex_matching(st, rex, sidx, ridx):
    
    if sidx >= len(st) and ridx >= len(rex):
        return True
    
    if sidx >= len(st) or ridx >= len(rex):
        return False
    
    if ridx<len(rex)-1:
        if rex[ridx+1] == '*':
            if st[sidx] == rex[ridx]:
                if sidx == len(st) - 1 and ridx == len(rex) -2: 
                    return True
                return regex_matching(st,rex,sidx,ridx+2) or regex_matching(st,rex, sidx+1, ridx)
            elif rex[ridx] == '.':
                if sidx == len(st) -1:
                    if ridx == len(rex) -2:
                        return True
                    elif rex[ridx + 2] == st[sidx] and ridx == len(rex) -3:
                        return True
                    else:
                        return False
                if ridx == len(rex) -2:
                    rex_copy = rex[:ridx] + st[sidx] + rex[ridx + 1:]
                    return regex_matching(st,rex_copy,sidx+1, ridx)

                
                rex_copy = rex[:ridx] + st[sidx] + rex[ridx + 1:]
                
                v1 = regex_matching(st,rex_copy,sidx+1,ridx)
                v2 = regex_matching(st,rex_copy,sidx+1,ridx+2)
                v3 = regex_matching(st,rex_copy,sidx,ridx+2)
                return v1 or v2 or v3
            elif ridx+2< len(rex):
                if st[sidx] == rex[ridx+2]:
                    return regex_matching(st,rex,sidx,ridx+2)
            else:
                return False

    if rex[ridx] == '.' or rex[ridx] == st[sidx]:
        return regex_matching(st,rex,sidx+1,ridx+1)
    
    return False
    
print(regex_matching(st, rex, 0, 0))
