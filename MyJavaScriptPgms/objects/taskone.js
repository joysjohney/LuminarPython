// sample input : HHHPPSDAAA
// sample output: 3H2P1S1D3A

var str="HHHPPSDAAA"

var cnt={}
for(ch of str)
    {
    if(ch in cnt) // H in cnt H
        {
        cnt[ch]+=1 // {H:2}
        }
        else
        {
        cnt[ch]=1; //{H:1}
        }
    }
var output=""
for (key in cnt)
    {
    output=output+cnt[key]+key
    }
console.log(output)