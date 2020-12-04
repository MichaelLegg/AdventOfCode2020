import data from "../data";
import exampleData from "../exampleData";

const start = process.hrtime();

function treeCounter(input: string[], increment: number, skip: boolean) {
    let count = increment;
    let treeCount = 0;
    let x = 0;
    for(skip ? x=2 : x=1; x < input.length; skip ? x+=2 : x++) {
        if(count >= input[x].length) {
            let original = input[x];
            let i = original.length;
            do {
                input[x] += original;
                i += original.length;
            } while(count >= i)
            if(input[x].charAt(count) === "#") treeCount++;
        } else if((count <= input[x].length) && input[x].charAt(count) === "#") treeCount++;
        count += increment;
    }
    return treeCount;
}
let answer = treeCounter(data, 1, false) * treeCounter(data, 3, false) * treeCounter(data, 5, false) * treeCounter(data, 7, false) * treeCounter(data, 1, true);
console.log("Puzzle answer: " + answer);

const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);