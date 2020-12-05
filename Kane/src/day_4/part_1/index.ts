import { createInterface } from "readline";
import { createReadStream} from "fs";
import { readFileSync} from "fs";

async function processLineByLine() {
  let data = "";

  const rl = createInterface({
    input: createReadStream("src/day_4/data.txt"),
    // crlfDelay: 100
  });

  for await (const line of rl) {
    data += line;
  }

  console.log(data.split("(?m)^\\s*$"));
}

// processLineByLine();

try {
    const data = readFileSync("src/day_4/data.txt", {encoding: 'utf8'});
    const lines = data.split(/\n\n/);

    // lines.forEach((line) => {
    //     // console.log(line);
    // });

    console.log(lines);
} catch (err) {
    console.error(err);
}

const start = process.hrtime();

function validatePassport(input: string[]) {
    return console.log(input);
}
// console.log("Puzzle answer: " + validatePassport());

const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);