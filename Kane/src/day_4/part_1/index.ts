import { createInterface } from "readline";
import { createReadStream} from "fs";

const stream = createReadStream("src/day_4/data.txt");
function streamToString (stream) {
    const chunks = []
    return new Promise((resolve, reject) => {
        stream.on('data', chunk => chunks.push(chunk))
        stream.on('error', reject)
        stream.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')))
    })
}

const start = process.hrtime();

async function validatePassport() {
    let result = await streamToString(stream);
    console.log(result);
    // return result;
}
validatePassport();
// console.log("Puzzle answer: " + validatePassport());

const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);