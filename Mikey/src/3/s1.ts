import Fs from "fs"

export default function Solution(): number{
    let numMatches = 0;
    let input: string[] = Fs.readFileSync(`src/3/data.txt`).toString().split('\r\n').filter(x => x.length > 0);
  
    let yCounter = 0;
    let rowLength = input[0].length;
    
    for(let line of input){
        if(line[yCounter] === '#') 
            numMatches++

        yCounter+=3;
        const remainder = yCounter - rowLength;
        if(remainder >= 0)
            yCounter = remainder        
    }       
    return numMatches;
}