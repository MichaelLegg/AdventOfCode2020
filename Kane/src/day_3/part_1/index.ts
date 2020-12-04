import data from "../data";
import exampleData from "../exampleData";

const start = process.hrtime();

function pwdPolicyCheck(input: string[]) {
    let count = 3;
    let treeCount = 0;
    for(let x=1; x < input.length; x++) {
        if(count >= input[x].length) {
            let original = input[x];
            let i = original.length;
            do {
                input[x] += original;
                i += original.length;
            } while(count >= i)
            if(input[x].charAt(count) === "#") treeCount++;
        } else if((count <= input[x].length) && input[x].charAt(count) === "#") treeCount++;
        count += 3;
    }
    return treeCount;
}
console.log("Puzzle answer: " + pwdPolicyCheck(data));

const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);