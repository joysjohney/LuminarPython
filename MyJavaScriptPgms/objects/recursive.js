 var str="ABACABAACCAB"
var order={}
for (char of str)
{
    if (char in order)
    {
    order[char]+=1
    }
    else
    {
    order[char]=1
    }

}
console.log(char)