import { createInterface } from "readline";
import { createReadStream} from "fs";

async function processLineByLine() {
  const rl = createInterface({
    input: createReadStream("src/day_6/testData.txt"),
    crlfDelay: Infinity
  });

  let data = [];
  let tempArr = [];
  let groups = [];
  let sumCounts = 0;

  for await (const line of rl) {
    data.push(line);
  }

  data.forEach((line, idx) => {
    if(line !== "") {
       tempArr.push(line);

      if(idx + 1 === data.length) {
        groups.push(tempArr);
        tempArr = [];
      }
    } else {
      groups.push(tempArr);
      tempArr = [];
    }
  });

  console.log(groups);

  return console.log("Puzzle answer: " + sumCounts);
}

const start = process.hrtime();

processLineByLine();

const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);