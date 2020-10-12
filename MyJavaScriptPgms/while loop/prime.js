var low=Number(prompt("enter lower limit :"));
var limit=Number(prompt("enter higher limit :"));

while(low<=limit){
    if(low%2==0){
        console.log(low);
	}
    low+=1;
}