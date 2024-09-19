# Author: Jose Bianchi
# GitHub username: josebianchi7

def superDigit(n, k):
    """
    Given an number string, n, and and int k.
    Add individual digits of n, multiply result by k, to get new_n.
    
    Repeat summation of individual digits until result is 1 digit (sum < 10)
    
    param n (str): number string to begin final int sequence
    param k (int): number of times n must be concatenated to create final int
    
    return (int): 'super digit', which is when new_n < 10
    """
        
    # Create initial super digit:
    curr_sum = 0
    for i in range(len(n)):
        curr_sum += int(n[i])

    new_n = str(curr_sum * k)    
    
    # Keep calculating super digit until result is 1 digit (less than 10)
    while len(new_n) > 1:
    
        curr_sum = 0
        for i in range(len(new_n)):
            curr_sum += int(new_n[i])

        if curr_sum < 10:
            return curr_sum

        # Reset string to latest super digit       
        new_n = str(curr_sum)
    
    # If initial super digit is less than 10, return result 
    return int(new_n)    


# Test cases:
if __name__ == '__main__':
    result1 = superDigit('9875', 4)
    print(result1)
    str2 = '7404954009694227446246375747227852213692570890717884174001587537145838723390362624487926131161112710589127423098959327020544003395792482625191721603328307774998124389641069884634086849138515079220750462317357487762780480576640689175346956135668451835480490089962406773267569650663927778867764315211280625033388271518264961090111547480467065229843613873499846390257375933040086863430523668050046930387013897062106309406874425001127890574986610018093859693455518413268914361859000614904461902442822577552997680098389183082654625098817411306985010658756762152160904278169491634807464356130877526392725432086439934006728914411061861235300979536190100734360684054557448454640750198466877185875290011114667186730452681943043971812380628117527172389889545776779555664826488520325234792648448625225364535053605515386730925070072896004645416713682004600636574389040662827182696337187610904694029221880801372864040345567230941110986028568372710970460116491983700312243090679537497139499778923997433720159174153'
    result2 = superDigit(str2, 100000)
    print(result2)
