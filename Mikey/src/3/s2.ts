import Fs from "fs"

interface rule {
    right: number;
    down: number;
}

export default function Solution(): number{
    let input: string[] = Fs.readFileSync(`src/3/data.txt`).toString().split('\r\n').filter(x => x.length > 0);

    let rules: rule[] = [{right: 1, down: 1}, {right:3, down:1}, {right: 5, down:1}, {right: 7, down: 1}, { right: 1, down: 2}]
  
    let rowLength = input[0].length;
    let total = 1;
    rules.forEach(rule => {
        let numMatches = 0;
        let yCounter = 0;

        for(let i = 0; i < input.length; i+=rule.down){
            if(input[i][yCounter] === '#') 
                numMatches++
    
            yCounter+=rule.right;
            const remainder = yCounter - rowLength;
            if(remainder >= 0)
                yCounter = remainder        
        }  
        total*=numMatches;
    });
       
    return total;
}